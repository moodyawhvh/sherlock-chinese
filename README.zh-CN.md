# sherlock 中文文档

[![原项目](https://img.shields.io/badge/原项目-sherlock--project--sherlock-blue?style=flat-square&logo=github)](https://github.com/sherlock-project/sherlock)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

> 本文是 [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) 官方 README 的中文翻译,只覆盖核心章节(简介 / 安装 / 使用)。完整内容以原项目为准。

## 简介

sherlock 通过用户名在 [400+ 社交网络](https://sherlockproject.xyz/sites)中查找对应账号,是经典的 OSINT 用户名枚举工具。

## 安装

> [!WARNING]
> 第三方维护的 ParrotOS 和 Ubuntu 24.04 软件包目前似乎已损坏,这些系统的用户请改用 `uv` / `pipx` / `pip` 或 Docker。

| 方式 | 说明 |
| - | - |
| `pipx install sherlock-project` | 可用 `pip` 或 [uv](https://docs.astral.sh/uv/) 代替 `pipx` |
| `docker run -it --rm sherlock/sherlock` | Docker 方式运行 |
| `dnf install sherlock-project` | Fedora/RHEL 系包管理器 |

社区还维护了 Debian(>= 13)、Ubuntu(>= 22.10)、Homebrew、Kali、BlackArch 的软件包,但这些包不由 Sherlock Project 直接支持或维护。

更多安装方式见官方文档:https://sherlockproject.xyz/installation

## 基本用法

只查一个用户:

```bash
sherlock user123
```

一次查多个用户:

```bash
sherlock user1 user2 user3
```

查到的账号会各自保存到以用户名命名的文本文件中(如 `user123.txt`)。

## 常用参数速查

```console
$ sherlock --help
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT] [--output OUTPUT] [--csv] [--xlsx] [--site SITE_NAME] [--proxy PROXY_URL] [--dump-response]
                [--json JSON_FILE] [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color] [--browse] [--local] [--nsfw] [--txt] [--ignore-exclusions]
                USERNAMES [USERNAMES ...]

positional arguments:
  USERNAMES             一个或多个要检查的用户名;用 {?} 可枚举相似用户名(替换为 '_'、'-'、'.')。

options:
  -h, --help            显示帮助信息并退出
  --version             显示版本与依赖信息
  --verbose, -v, -d     显示额外调试信息与指标
  --folderoutput, -fo   多用户名时,结果统一保存到指定文件夹
  --output, -o          单用户名时,结果保存到指定文件
  --csv                 输出 CSV 文件
  --xlsx                输出 xlsx 表格
  --site SITE_NAME      只查询列出的站点,可多次指定
  --proxy, -p           通过代理发请求,如 socks5://127.0.0.1:1080
  --dump-response       把 HTTP 响应打印到终端,便于针对性调试
  --json, -j            从本地或在线 JSON 文件加载站点数据(也接受上游 PR 编号)
  --timeout             每个请求的等待秒数(默认 60)
  --print-all           同时输出未命中的站点
  --print-found         只输出命中的站点
  --no-color            终端输出不着色
  --browse, -b          用默认浏览器打开所有结果
  --local, -l           强制使用本地 data.json
  --nsfw                在默认列表中包含 NSFW 站点
  --txt                 生成 txt 结果文件
  --ignore-exclusions   忽略上游排除规则(可能产生更多误报)
```

## 相关链接

- 官网:https://sherlock-project.github.io/
- 安装文档:https://sherlockproject.xyz/installation
- 使用文档:https://sherlockproject.xyz/usage
- 参与贡献:https://sherlockproject.xyz/contribute

## 许可证与版权

MIT © Sherlock Project,作者 [Siddharth Dushantha](https://github.com/sdushantha)。

---

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

本项目为 [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) 的中文翻译,所有代码版权归原项目作者所有,遵循其原始许可证。**如果觉得有用,请给原项目点个 Star!** ⭐
