<div align="center">

# sherlock 中文翻译版

**[中文版] sherlock — 通过用户名在 400+ 社交网络中 Hunt 账号的 OSINT 调查工具**

[![原项目](https://img.shields.io/badge/原项目-sherlock--project--sherlock-blue?style=flat-square&logo=github)](https://github.com/sherlock-project/sherlock)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/sherlock-project/sherlock?style=flat-square&label=原项目Stars)](https://github.com/sherlock-project/sherlock/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/sherlock-project/sherlock

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

sherlock 是一款开源 OSINT(开源情报)调查工具,只需输入一个用户名,即可自动在 400+ 个社交网络和网站上查找该用户名被注册的账号。它会向各站点发起请求并判断"用户名已存在"的页面特征,把命中的结果整理输出,是社工调查、安全研究和账号足迹排查的经典利器。

## ✨ 主要特性

- 一条命令即可在 400+ 社交网络中按用户名 Hunt 账号
- 支持一次批量查询多个用户名
- 使用 `{}` 占位符自动枚举相似用户名(替换为 `_`、`-`、`.`)
- 结果自动保存为以用户名命名的 txt 文件,支持 CSV / XLSX 导出
- 支持 `--site` 只查询指定站点,`--json` 加载自定义站点列表
- 支持通过 `--proxy` 走 SOCKS/HTTP 代理发起请求
- 可调超时时间、彩色/无色终端输出、`--print-all` / `--print-found` 控制结果展示
- 支持 `--browse` 直接在浏览器打开所有命中结果
- 内置 NSFW 站点开关,默认不检查敏感站点
- 安装方式丰富:pipx / pip / uv、Docker、dnf,以及 Debian、Ubuntu、Homebrew、Kali、BlackArch 等社区包

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

1. 安装(推荐 pipx,也可用 pip 或 uv):

```bash
pipx install sherlock-project
```

2. 或者用 Docker 直接运行:

```bash
docker run -it --rm sherlock/sherlock
```

3. 查询单个用户名:

```bash
sherlock user123
```

4. 批量查询多个用户名:

```bash
sherlock user1 user2 user3
```

5. 查看全部命令行参数:

```bash
sherlock --help
```

6. 走代理查询(示例):

```bash
sherlock user123 --proxy socks5://127.0.0.1:1080
```

查到的账号会自动保存到以用户名命名的文本文件(如 `user123.txt`)。

完整源代码与最新版本请访问原项目:https://github.com/sherlock-project/sherlock

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**如果觉得有用,请给原项目点个 Star!** ⭐
