---
layout: post
title: 使用GitBash的ssh服务
tags: 
  - git
  - ssh
categories:

---
## 前言
今天在观看b站的Django教学视频的时候，发现git提供了ssh连接服务。也就是说，或许可以不安装Xshell来连接ssh了！
<!-- more -->
### ssh命令

首先，在window中通过鼠标**右键**来打开**git bash命令行**。

![kVjjmD.png](https://s2.ax1x.com/2019/01/24/kVjjmD.png)
然后，使用git提供的ssh命令：

```shell
ssh username@ipaddress -p 28002
```

`username`是linux系统的用户名，`ipaddress`是linux服务器的ip地址，`-p 28002`用来指定端口号(如果不指定，则默认为22)。输入命令后，如果服务器能连0上，会提示你输入密码。输入正确的密码之后，就能成功登录了。
![kVvd91.png](https://s2.ax1x.com/2019/01/24/kVvd91.png)

### bat脚本登录

如果每次都要执行上面的操作，未免有些太麻烦。我们可以写一个bat脚本来快速登录。

但是，在此之前我们分析一下实现方法。大致步骤：

- 打开git bash命令行
- 在git bash命令行输入ssh登录命令

那么，问题来了，我们使用bat脚本运行打开一个git bash窗口之后，要如何再向gitBash命令行中输入命令呢？我的解决方法是：

git安装目录下，有个cmd文件夹，只需把要在gitbash命令行中运行的命令（就是ssh登录命令）写成文件保存，就可以通过文件直接登录了。换句话说，git安装目录中cmd文件夹下的文件，即是git的”bat脚本“(这里的脚本是.cmd格式)。

现在，再cmd目录下创建一个cmd脚本，然后保存。

![kVvhgP.png](https://s2.ax1x.com/2019/01/24/kVvhgP.png)

我们只要运行这个cmd文件，就可以实现**一键登录Linux**了~~~

> 解决方法参考自：https://www.zhihu.com/question/38962022