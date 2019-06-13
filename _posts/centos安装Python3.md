---
title: centos安装Python3
tags:
  - linux
  - python
date: 2018-10-29 22:04:28
---

## 前言

在阿里云租用了云服务器。想安装python3学习django框架的时候，发现centos自带了python2.7.5.但是我们需要python3.5以上版本。从网上找到linux-centos7安装python3并与python2共存的教程，在此记录一下。

> 引用自:https://www.cnblogs.com/JahanGu/p/7452527.html

## 查看python版本

CentOS 7.2 默认安装了python2.7.5，因为一些命令要使用它(比如`yum`命令)。

使用`python -V`命令查看是否安装了python

![](/img/201810291.jpg)

然后使用`which python`命令查看python可执行文件的位置

![](/img/1540823226.jpg)

可见，执行文件在/usr/bin目录下。接着，我们用`cd /usr/bin`切换到该目录

然后，使用`ls -l python*`命令查看

![](/img/201810293.jpg)

因为我们要安装python3版本，所以python要指向python3才行，目前还没有安装python3，先备份,备份之前先安装相关包，用于下载编译python3。不能忽略相关包
`yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make`

然后备份`mv python python.bak`

## 编译安装python3

去官网下载编译安装包:`wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz`

解压缩:`xz -d Python-3.6.2.tar.xz`

解tar包:`tar -xf ./Python-3.6.2.tar`

`cd Python-3.6.2`进入路径

执行下面的命令编译安装

- `./configure prefix=/usr/local/python3`
- `make && make install`

安装成功后，/usr/local/目录下就会有python3了

![](/img/201810294.jpg)

## 添加软链

接下来，我们添加软链到执行目录`/usr/bin`下。使用`ln -s /usr/local/python3/bin/python3 /usr/bin/python`命令。

测试一下是否成功。执行：
- `python -V`  看看输出的是不是python3的版本
- `python2 -V`  看看输出的是不是python2的版本

## 其他修改

因为执行yum需要python2版本，所以我们还要修改yum的配置，执行：`vim /usr/bin/yum`,把"#! /usr/bin/python"修改为"#! /usr/bin/python2".

同理 `vi /usr/libexec/urlgrabber-ext-down` 文件里面的"#! /usr/bin/python" 也要修改为"#! /usr/bin/python2".

这样python3版本就安装完成；同时python2也存在

python -V   版本3 

python2 -V 版本2

## pip和pip3

即使我们安装了python3，但是pip命令还是指向python2环境。因此，要想使用pip安装库到python3环境，我们还需要修改一下pip。
执行`ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3`命令，把pip3命令添加到执行路径。
然后我们使用pip3就可以安装库到python3环境了。例如：使用`pip3 install django`来安装django库到python3环境中。

这样使用pip命令可以安装库到python2环境，使用pip3命令可以安装库到python3环境！