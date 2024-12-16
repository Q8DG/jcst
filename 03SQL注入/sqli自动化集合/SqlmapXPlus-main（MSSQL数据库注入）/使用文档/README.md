简介

今日，某安全博主二开了SQLmapXPlus版本

目前开发现状

目前已完成部分二开，包括ole、xpcmdshell两种文件上传、内存马上传、clr安装功能，能够实现mssql注入场景下的自动化注入内存马、自动化提权、自动化添加后门用户、自动化远程文件下载、自动化shellcode加载功能。

新增功能

```
#  开启 clr 功能
--enable-clr#  关闭 clr 功能--disable-clr
# 通过 xp_cmdshell 实现的文件上传功能 ，作用为将本地文件上传到远程服务器--xp-upload localfile remotefile
# 通过 ole 实现的文件上传功能 ，作用为将本地文件上传到远程服务器--ole-upload#  通过 xp_cmdshell 实现的clr安装方式--install-clr1
#  通过 ole 实现的clr安装方式--install-clr2
#  进入clr-shell命令交互模式--clr-shell
#  通过 xp_cmdshell 实现的HttpListener内存马上传方式--sharpshell-upload1#  通过 ole 实现的HttpListener内存马上传方式--sharpshell-upload2
```

使用教程

```
git clone https://github.com/co01cat/SqlmapXPlus
```

或者直接下载

![图片](./assets/640.png)

然后解压，

运行python sqlmap.py -hh

![图片](./assets/640-1709218479576-1.png)

该师傅发表了使用文档

[数据库注入工具 SqlmapXPlus ！增强MSSQL后渗透利用方式！](http://mp.weixin.qq.com/s?__biz=Mzk0NjYyNDI0Ng==&mid=2247483828&idx=1&sn=5735814837f8e58376187668714e4605&chksm=c302022df4758b3ba5e4368c3f8be2ac5183ebbebc247e318380b9e14ae341d717e59102e448&scene=21#wechat_redirect)



文章介绍了SqlmapXPlus这一工具，它是在经典的数据库漏洞利用工具Sqlmap的基础上，经过二次开发而成，特别增强了对MSSQL数据库注入的攻击能力。SqlmapXPlus增加了多项新功能，包括文件上传、内存马上传、CLR安装等，以支持在各种限制性的网络环境下进行SQL Server注入攻击，并能完成自动化的攻击流程。

特别地，工具解决了在不出网、低权限、站库分离等复杂环境中的一些常见问题，并提供了一系列的攻击和提权功能，如自动化注入内存马、提权、添加后门用户、远程文件下载及shellcode加载。

新增功能详细介绍了CLR的开启与关闭、文件上传（通过xp_cmdshell和ole实现）、CLR安装方式（通过xp_cmdshell和ole实现），以及内存马的上传。此外，还介绍了clr-shell命令交互模式的内置功能，如开启远程桌面、添加用户、命令执行、提权、内存马注入、文件下载等。

文章还提供了具体的使用示例和命令格式，指导用户如何安装CLR、上传内存马、进入clr-shell模式，并执行各种操作，最终实现攻击目的。同时，说明了如何使用cobaltstrike生成shellcode，并通过SqlmapXPlus的功能将其注入到目标系统中。

总结来说，文章详细阐述了SqlmapXPlus这一强化版的Sqlmap工具的新功能和使用场景，为数据库攻击提供了更多自动化和应对复杂环境的解决方案。