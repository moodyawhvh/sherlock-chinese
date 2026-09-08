"""Sherlock 站点信息模块(Sites Information Module)

本模块用于存储网站相关信息。
这些是用于搜索用户名的原始数据。
"""
import json
import requests
import secrets


# 站点清单(manifest)数据源:在线 data.json
MANIFEST_URL = "https://data.sherlockproject.xyz"
# 误报排除清单:从仓库 exculsions 分支拉取,这些站点会被从结果中剔除
EXCLUSIONS_URL = "https://raw.githubusercontent.com/sherlock-project/sherlock/refs/heads/exclusions/false_positive_exclusions.txt"

class SiteInformation:
    def __init__(self, name, url_home, url_username_format, username_claimed,
                information, is_nsfw, username_unclaimed=secrets.token_urlsafe(10)):
        """创建站点信息对象(Site Information)。

        保存某个特定网站的相关信息。

        关键字参数:
        self                   -- 本对象自身。
        name                   -- 标识站点的字符串。
        url_home               -- 站点主页 URL 字符串。
        url_username_format    -- 站点上用户名 URL 格式字符串。
                                  注意:该字符串应包含占位符 "{}",
                                  用户名会被替换到该位置。例如
                                  "https://somesite.com/users/{}" 表示
                                  各个用户名的页面位于网站的
                                  "https://somesite.com/users/" 区域下。
        username_claimed       -- 已知在站点上被占用的用户名字符串。
        username_unclaimed     -- 已知在站点上未被占用的用户名字符串。
        information            -- 包含该网站全部已知信息的字典。
                                  注意:关于如何实际检测用户名是否存在的
                                  自定义信息也包含在该字典中。这些信息由
                                  检测方法使用,但仅记录在本对象中留作后用。
        is_nsfw                -- 布尔值,指示该站点是否为 NSFW(不适合工作场所)。

        返回值:
        无。
        """

        self.name = name
        self.url_home = url_home
        self.url_username_format = url_username_format

        self.username_claimed = username_claimed
        # 未占用用户名统一用随机 token,避免调用方传入的值造成误判
        self.username_unclaimed = secrets.token_urlsafe(32)
        self.information = information
        self.is_nsfw  = is_nsfw

        return

    def __str__(self):
        """将对象转换为字符串。

        关键字参数:
        self                   -- 本对象自身。

        返回值:
        格式良好的字符串,用于展示本对象的信息。
        """

        return f"{self.name} ({self.url_home})"


class SitesInformation:
    def __init__(
            self,
            data_file_path: str|None = None,
            honor_exclusions: bool = True,
            do_not_exclude: list[str] = [],
        ):
        """创建站点集合信息对象(Sites Information)。

        保存所有受支持网站的信息。

        关键字参数:
        self                   -- 本对象自身。
        data_file_path         -- 指示数据文件路径的字符串。
                                  文件名必须以 ".json" 结尾。

                                  支持三种格式:
                                   * 绝对路径格式
                                     例如 "c:/stuff/data.json"。
                                   * 相对路径格式
                                     以当前工作目录为基准。
                                     例如 "data.json"。
                                   * URL 格式
                                     例如
                                     "https://example.com/data.json" 或
                                     "http://example.com/data.json"。

                                  如果数据文件路径不符合预期格式,
                                  或加载文件时出现任何问题,都会抛出异常。

                                  如果未指定该选项,则使用默认站点列表。

        返回值:
        无。
        """

        if not data_file_path:
            # 默认数据文件是 GitHub 仓库中的在线 data.json。使用它而非本地文件的
            # 原因是让用户拿到最新的数据,避免用户再提交那些误报早已修复、
            # 或数据已过期的 issue
            data_file_path = MANIFEST_URL

        if data_file_path.lower().startswith("http"):
            # 引用的是一个 URL。
            try:
                response = requests.get(url=data_file_path, timeout=30)
            except Exception as error:
                raise FileNotFoundError(
                    f"Problem while attempting to access data file URL '{data_file_path}':  {error}"
                )

            if response.status_code != 200:
                raise FileNotFoundError(f"Bad response while accessing "
                                        f"data file URL '{data_file_path}'."
                                        )
            try:
                site_data = response.json()
            except Exception as error:
                raise ValueError(
                    f"Problem parsing json contents at '{data_file_path}':  {error}."
                )

        else:
            # 引用的是本地文件。
            try:
                with open(data_file_path, "r", encoding="utf-8") as file:
                    try:
                        site_data = json.load(file)
                    except Exception as error:
                        raise ValueError(
                            f"Problem parsing json contents at '{data_file_path}':  {error}."
                        )

            except FileNotFoundError:
                raise FileNotFoundError(f"Problem while attempting to access "
                                        f"data file '{data_file_path}'."
                                        )

        # 移除 JSON Schema 声明字段,它不是站点条目
        site_data.pop('$schema', None)

        if honor_exclusions:
            try:
                # 拉取误报排除清单,并将其中站点从数据中剔除
                response = requests.get(url=EXCLUSIONS_URL, timeout=10)
                if response.status_code == 200:
                    exclusions = response.text.splitlines()
                    exclusions = [exclusion.strip() for exclusion in exclusions]

                    # do_not_exclude 中的站点即使出现在清单里也不剔除
                    for site in do_not_exclude:
                        if site in exclusions:
                            exclusions.remove(site)

                    for exclusion in exclusions:
                        try:
                            site_data.pop(exclusion, None)
                        except KeyError:
                            pass

            except Exception:
                # 加载排除清单出现任何问题时,直接不带排除继续运行
                print("Warning: Could not load exclusions, continuing without them.")
                honor_exclusions = False

        self.sites = {}

        # 将 JSON 文件中的所有站点信息加入内部站点列表。
        for site_name in site_data:
            try:

                self.sites[site_name] = \
                    SiteInformation(site_name,
                                    site_data[site_name]["urlMain"],
                                    site_data[site_name]["url"],
                                    site_data[site_name]["username_claimed"],
                                    site_data[site_name],
                                    site_data[site_name].get("isNSFW",False)

                                    )
            except KeyError as error:
                raise ValueError(
                    f"Problem parsing json contents at '{data_file_path}':  Missing attribute {error}."
                )
            except TypeError:
                print(f"Encountered TypeError parsing json contents for target '{site_name}' at {data_file_path}\nSkipping target.\n")

        return

    def remove_nsfw_sites(self, do_not_remove: list = []):
        """
        从站点集合中移除 NSFW 站点,即 isNSFW 标记为真的站点

        关键字参数:
        self                   -- 本对象自身。

        返回值:
        无
        """
        sites = {}
        do_not_remove = [site.casefold() for site in do_not_remove]
        for site in self.sites:
            if self.sites[site].is_nsfw and site.casefold() not in do_not_remove:
                continue
            sites[site] = self.sites[site]
        self.sites =  sites

    def site_name_list(self):
        """获取站点名称列表。

        关键字参数:
        self                   -- 本对象自身。

        返回值:
        由站点名称字符串组成的列表。
        """

        return sorted([site.name for site in self], key=str.lower)

    def __iter__(self):
        """对象的迭代器。

        关键字参数:
        self                   -- 本对象自身。

        返回值:
        站点对象的迭代器。
        """

        for site_name in self.sites:
            yield self.sites[site_name]

    def __len__(self):
        """对象长度。

        关键字参数:
        self                   -- 本对象自身。

        返回值:
        站点对象的长度。
        """
        return len(self.sites)
