---
layout: post
title: 一、【fiddler】的安装与配置
tags:
  - fiddler
date: 2018-07-30 16:02:17
---

### 0 前言

Fiddler是最强大最好用的Web调试工具之一，它能记录所有客户端和服务器的http和https请求，允许你监视，设置断点，甚至修改输入输出数据，Fiddler包含了一个强大的基于事件脚本的子系统，并且能使用.net语言进行扩展。你对HTTP 协议越了解， 你就能越掌握Fiddler的使用方法。你越使用Fiddler，就越能帮助你了解HTTP协议。Fiddler无论对开发人员或者测试人员来说，都是非常有用的工具。

之前了解了fiddler的基本使用方法。在补充复习fiddler知识的基础上，进一步学习fiddler的使用。

想要全面的学习fiddler，最好的方式还是看[官方文档](https://docs.telerik.com/fiddler/Configure-Fiddler/)来学习。如果官网的网页太慢，可以观看在github上开源的文档。我把开源库fork到了我的github上。点击[这里](https://github.com/Ngwind/fiddler-docs)查看。

---

### 1 fiddler的工作原理

Fiddler 是以代理web服务器的形式工作的，它使用代理地址:127.0.0.1，端口:8888。当Fiddler退出的时候它会自动注销，这样就不会影响别的程序。不过如果Fiddler非正常退出，这时候因为Fiddler没有自动注销，会造成网页无法访问。解决的办法是重新启动下Fiddler。

![fiddler代理](/img/2018-07-30 162723.png)

### 2 下载Fiddler

在[官网](https://www.telerik.com/fiddler)上下载最新的Fiddler安装包。最好下载高版本的，之前我下载安装的是Fiddler2，然后里面有些功能（比如Fiddler Script功能）还要安装插件。

在官网找到Free download按钮，点击进入下载页面。下载前，它会让你填写一下基本信息，随便填写好之后，就可以下载了。

### 3 安装Fiddler

一般下载的是一个.exe的可执行文件，下载好安装包之后，点击FiddlerSetup.exe开始安装。点击同意使用协议->选择安装路径（尽量别安装在C盘）->点击开始安装，稍等片刻就安装完成了。

### 4 使用之前

Fiddler代理服务器是安装在Fiddler中的，它作为中间人，抓取客户端发送的数据包，然后转发到真正的请求服务器；服务器向fiddler代理服务器返回响应数据包，然后fiddler代理服务器再转发给客户端。一些特殊的场景需要我们进行配置比如：解析Https数据包、使用通道绑定令牌进行身份验证等

#### 4.1 解析Https数据包

第一步，点击选项栏的Tools->Options->Https.

第二步，勾选Decrypt HTTPS Traffic，前提是确保你勾选了Capture Https connects。

![](/img/2018-07-30 165127.png)

此外，可以在下方的文本框里输入域名，来跳过特定网址的https解析。

![](/img/2018-07-30 165420.png)

#### 4.2 浏览器抓包

fiddler默认是在本机的8888端口监听数据包，所以要想能够抓到浏览器发出的包，需要我们在浏览器的设置中配置好代理（ip是本机ip：127.0.0.1，端口默认8888）。有些浏览器可能会自动设置好代理，比如IE浏览器、谷歌浏览器等。

#### 4.3 移动设备抓包

fiddler也可以抓取移动设备上的数据包，前提是你使用fiddler的电脑和移动设备要在同一个局域网中。我们一般通过手机连接wifi来抓包。这时需要我们给移动设备安装证书。

##### 4.3.1 fiddler中的设置

1. 点击Tools > Fiddler Options > Connections.

2. 勾选 Allow remote computers to connect. 
   ![](/img/2018-07-30 170837.png)

3. 然后重启fiddler

4. fiddler右上角有个Online的电脑图标，把鼠标移到上面，会显示fiddler服务器的IP地址。记得这个IP地址，稍后会用上。
   ![](/img/2018-07-30 171035.png)

##### 4.3.2 移动设备中的设置

1. 打开wifi，连接上局域网wifi。
2. 选择修改wifi网络，把代理改为手动
3. 设置代理ip地址为fiddler服务器的地址，端口号默认8888。可以在fiddler->Tools->connections中查看端口号。
4. 设置完成后记得点击保存。
5. 可以用手机浏览器访问`你的fiddler的ip地址:端口号`进行验证。这时fiddler中应该可以看到手机发送的数据包。

##### 4.3.3 解析手机发送的https包

想要抓取到手机端发送的https协议包，我们还要进行一些操作

用手机浏览器访问`你的fiddler的ip地址:端口号`，点击页面中的FiddlerRoot certificate.这时会让你下载根证书，接受下载即可。
下载完成后，在手机的设置中安装证书（具体手机安装证书的地方不一样）。安装好之后，应该就可以抓取到手机中的https协议包了。

#### 4.4 其他

在使用完fiddler后，记得到代理设置里面取消代理。
