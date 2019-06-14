---
layout: post
title: 使用gh-pages+Hexo搭建个人网页教程
date: 2018-07-27 17:35:02
tags: 
  - hexo  
---

# 前言

使用github pages服务搭建博客的好处有：

1. 全是静态文件，访问速度快；
2. 免费方便，不用花一分钱就可以搭建一个自由的个人博客，不需要服务器不需要后台；
3. 可以随意绑定自己的域名，不仔细看的话根本看不出来你的网站是基于github的；
4. 数据绝对安全，基于github的版本管理，想恢复到哪个历史版本都行；
5. 博客内容可以轻松打包、转移、发布到其它平台；
6. 等等；

## 准备工作

确保你完成了下列准备：

* 有一个github账号，没有的话去注册一个；
* 安装了node.js、npm，并了解相关基础知识；
* 安装了git for windows（或者其它git客户端）

<!--more-->

# 搭建github博客

## 创建仓库

新建一个名为你的用户名.github.io的仓库，比如说，如果你的github用户名是Ngwind，那么你就新建Ngwinf.github.io的仓库（必须是你的用户名，其它名称无效），将来你的网站访问地址就是 [http://Ngwind.github.io](http://Ngwind.github.io) 了，是不是很方便？

## 绑定域名

当然，你不绑定域名肯定也是可以的，就用默认的 xxx.github.io 来访问，如果你想更个性一点，想拥有一个属于自己的域名，那也是OK的。

首先你要注册一个域名，域名注册以前总是推荐去godaddy，现在觉得其实国内的阿里云也挺不错的，价格也不贵，毕竟是大公司，放心！

# 配置SSH Key

为什么要配置这个呢？因为你提交代码肯定要拥有你的github权限才可以，但是直接使用用户名和密码太不安全了，所以我们使用ssh key来解决本地和服务器的连接问题。

用git bash执行如下命令：

`$ cd ~/. ssh #检查本机已存在的ssh密钥`

如果提示：No such file or directory 说明你是第一次使用git。

`ssh-keygen -t rsa -C "邮件地址"`

然后连续3次回车，最终会生成一个文件在用户目录下，打开用户目录，找到`.ssh\id_rsa.pub`文件，记事本打开并复制里面的内容，打开你的github主页，进入个人设置 -> SSH and GPG keys -> New SSH key：

## 测试是否成功

等后面上传代码带github时，再验证吧~

此时你还需要配置：

```git
$ git config --global user.name "liuxianan"// 你的github用户名，非昵称
$ git config --global user.email  "xxx@qq.com"// 填写你的github注册邮箱

```

# 使用hexo写博客

## hexo简介

Hexo是一个简单、快速、强大的基于 Github Pages 的博客发布工具，支持Markdown格式，有众多优秀插件和主题。

官网： http://hexo.io

github: https://github.com/hexojs/hexo

## 原理

由于github pages存放的都是静态文件，博客存放的不只是文章内容，还有文章列表、分类、标签、翻页等动态内容，假如每次写完一篇文章都要手动更新博文目录和相关链接信息，相信谁都会疯掉，所以hexo所做的就是将这些md文件都放在本地，每次写完文章后调用写好的命令来批量完成相关页面的生成，然后再将有改动的页面提交到github。

## 注意事项

安装之前先来说几个注意事项：

1. 很多命令既可以用Windows的cmd来完成，也可以使用git bash来完成，但是部分命令会有一些问题，为避免不必要的问题，建议全部使用git bash来执行；
1. hexo不同版本差别比较大，网上很多文章的配置信息都是基于2.x的，所以注意不要被误导；
1. hexo有2种_config.yml文件，一个是根目录下的全局的_config.yml，一个是各个theme下的；

## 安装

打开gitbash，运行下面的命令：

`$ npm install -g hexo`

## 初始化

在电脑的某个地方新建一个名为hexo的文件夹（名字可以随便取），比如我的是F:\Workspaces\hexo，由于这个文件夹将来就作为你存放代码的地方，所以最好不要随便放。

```git
$ cd /f/Workspaces/hexo/
$ hexo init
```

hexo会自动下载一些文件到这个目录，包括node_modules.

接着执行以下命令：

```git
$ hexo g # 生成
$ hexo s # 启动服务
```

执行以上命令之后，hexo就会在public文件夹生成相关html文件，这些文件将来都是要提交到github去的.

`hexo s`是开启本地预览服务，打开浏览器访问 http://localhost:4000 即可看到内容，很多人会碰到浏览器一直在转圈但是就是加载不出来的问题，一般情况下是因为端口占用的缘故，因为4000这个端口太常见了，解决端口冲突问题请参考这篇文章：

http://blog.liuxianan.com/windows-port-bind.html

第一次初始化的时候hexo已经帮我们写了一篇名为 Hello World 的文章，默认的主题比较丑，打开时就是这个样子：

![第一次的页面](http://image.liuxianan.com/201608/20160818_132443_202_6848.png)

## 修改主题

我们别的不做，首先来替换一个好看点的主题。这是 官方主题。

个人比较喜欢的2个主题：hexo-theme-jekyll 和 hexo-theme-yilia。

首先下载这个主题：

~~~git
$ cd /f/Workspaces/hexo/
$ git clone https://github.com/litten/hexo-theme-yilia.git themes/yilia

~~~

下载后的主题这都保存在hexo/themes文件夹中

修改_config.yml中的theme: landscape改为theme: yilia，然后重新执行hexo g来重新生成。

如果出现一些莫名其妙的问题，可以先执行hexo clean来清理一下public的内容，然后再来重新生成和发布。

## 上传之前

在上传代码到github之前，一定要记得先把你以前所有代码下载下来（虽然github有版本管理，但备份一下总是好的），因为从hexo提交代码时会把你以前的所有代码都删掉。

## 上传到github

如果你一切都配置好了，发布上传很容易，一句hexo d就搞定，当然关键还是你要把所有东西配置好。

首先，ssh key肯定要配置好。

其次，配置_config.yml中有关deploy的部分：

正确写法：

```git
deploy:
  type: git
  repository: git@github.com:liuxianan/liuxianan.github.io.git
  branch: master
```
错误写法：

```git
deploy:
  type: github
  repository: https://github.com/liuxianan/liuxianan.github.io.git
  branch: master
```
后面一种写法是hexo2.x的写法，现在已经不行了，无论是哪种写法，此时直接执行hexo d的话一般会报如下错误：
```git
Deployer not found: github 或者 Deployer not found: git
```
原因是还需要安装一个插件：
```git
npm install hexo-deployer-git --save
```
打开你的git bash，输入hexo d就会将本次有改动的代码全部提交，没有改动的不会：

![1](http://image.liuxianan.com/201608/20160818_140441_769_5024.png)

## 保留CNAME、README.md等文件

提交之后网页上一看，发现以前其它代码都没了，此时不要慌，一些非md文件可以把他们放到source文件夹下，这里的所有文件都会原样复制（除了md文件）到public目录的：

![2](http://image.liuxianan.com/201608/20160818_141037_580_8035.png)

由于hexo默认会把所有md文件都转换成html，包括README.md，所有需要每次生成之后、上传之前，手动将README.md复制到public目录，并删除README.html。

## 常用命令

常见命令
```
hexo new "postName" #新建文章
hexo new page "pageName" #新建页面
hexo generate #生成静态页面至public目录
hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy #部署到GitHub
hexo help  # 查看帮助
hexo version  #查看Hexo的版本
```
缩写：
```
hexo n == hexo new
hexo g == hexo generate
hexo s == hexo server
hexo d == hexo deploy
```
组合命令：
```
hexo s -g #生成并本地预览
hexo d -g #生成并上传
```

## _config.yml

这里面都是一些全局配置，每个参数的意思都比较简单明了，所以就不作详细介绍了。

需要特别注意的地方是，冒号后面必须有一个空格，否则可能会出问题。

## 写博客

定位到我们的hexo根目录，执行命令：
```
hexo new 'my-first-blog'
```
hexo会帮我们在_posts下生成相关md文件：
![3](http://image.liuxianan.com/201608/20160823_183047_352_1475.png)
我们只需要打开这个文件就可以开始写博客了.

当然你也可以直接自己新建md文件，用这个命令的好处是帮我们自动生成了时间。

一般完整格式如下：

```text
---
title: postName #文章页面上的显示名称，一般是中文
date: 2013-12-02 15:30:16 #文章生成时间，一般不改，当然也可以任意修改
categories: 默认分类 #分类
tags: [tag1,tag2,tag3] #文章标签，可空，多标签请用格式，注意:后面有个空格
description: 附加一段文章摘要，字数最好在140字以内，会出现在meta的description里面
---

以下是正文
```

### 写博客工具

我个人使用微软的vxcode

### 如何让博文列表不显示全部内容

默认情况下，生成的博文目录会显示全部的文章内容，如何设置文章摘要的长度呢？

答案是在合适的位置加上`<!--more-->`即可。

## 最终效果

参考我的网页：[这里](Ngwind.gihub.io)

## 参考

http://blog.haoji.me/build-blog-website-by-hexo-github.html?from=xa#ru-he-rang-bo-wen-lie-biao-bu-xian-shi-quan-bu-na-rong

http://www.cnblogs.com/zhcncn/p/4097881.html

http://www.jianshu.com/p/05289a4bc8b2