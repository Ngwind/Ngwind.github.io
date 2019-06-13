---
title: 三、【fiddler】之发送请求
tags:
  - fiddler
date: 2018-08-08 00:53:48
---

### 0 前言

fiddler是一个强大的抓包工具。不过除了使用它进行抓包分析，我们还能使用它来发送请求request。接下来介绍如何使用fiddler发送请求。

---

### 1 Composer

fiddler的左边tab栏中有一个"Composer"栏。正如它的名字意思："作曲家",我们在Composer中发送请求。点开Composer栏，它的界面组成如下图：

![](/img/2018-08-08 010342.jpg)

它有一个Execute按钮,当我们写好http请求后，点击按钮就可以发送请求了。不过先不急，我们先介绍它的4个tab栏：Parsed、Raw、Scratchpad、Options

#### 1.1 Parsed

点击进入Parsed，在这里我们能方便快速地编写请求。

![](/img/2018-08-08 012002.jpg)

- 在左上角可以选择请求方法。常用方法有：GET、POST、PUT、HEAD...
- 在中间输入你要请求的url。
- 然后在后面的框中选择http协议版本。
- 下面第一个文本框是填写头文件Header的。
- 底下的文本框用来填写body。选择POST方法，则可以编辑body文本框。还可以点击蓝色字‘upload file’来上传文件。
- 最右边可以看到之前发送过的请求。勾选了log requests就可以保存request请求记录

此外，我们可以直接把左边session list中的一个session拖到Composer中，点击execuet运行请求。

##### 示例

现在我们来演示一下：发送一个POST请求到https://postman-echo.com/post。

1. 选择POST方法
2. 输入url：`https://postman-echo.com/post`
3. 使用默认HTTP版本：http 1.1
4. 编辑请求header
   ```http
   User-Agent: Fiddler
   Content-Type: application/form-data
   Host: postman-echo.com
   ```
5. 编辑请求body
   ```http
   hello world!!!
   ```
6. 点击execute执行请求

![](/img/2018-08-08 013221.jpg)

结果是运行成功。可以在session list中看到我们发送了一条请求，在inspectors中查看详情：

![](/img/2018-08-08 014354.png)

#### 1.2 Raw

Composer中的第2个tab是Raw。我们可以在Raw中编写原始的http请求协议，然后点击execute发送请求。一般我们都不会这么编写吧...

如图，在Raw中编写原始http请求：

![](/img/2018-08-08 014844.jpg)

运行结果与上面使用parsed的示例中结果是一样的。

此外，Raw界面也支持直接把session拖拽进来运行。

#### 1.3 Scratchpad

Composer中的第3个tab是Scratchpad。正如它的中文意思：便签簿。这里可以储存你的请求。每个请求之间用“=========”来分开。你可以自己输入Raw格式的http请求，也可以直接从左边的会话中拖拽进来。

如果要运行一个请求：用鼠标划选一个请求（注意不要把====分隔符也选中了），然后点击execute就可以运行了。

![](/img/2018-08-08 020214.jpg)

#### 1.4 Options

Composer中的第4个tab是Options。这里是设置一些选项的地方。

![](/img/2018-08-08 022443.jpg)

分为`Request 选项`和`UI 选项`。

Request 选项：
- inspect session：如果勾选了这一项，那么在执行请求的时候，会自动切换到inspector界面。
- fix content-length header:勾选此项，会在你发送请求的时候帮你在请求头中修改content-Length属性（如果没有就创建），以匹配请求主体的大小。
- follow redirects：勾选此项，会跟随重定向。
- automactically authenticate：勾选此项，导致 Fiddler 自动响应 http / 401和 http / 407的挑战，这些挑战使用 NTLM 或协商协议使用当前用户的 Windows 凭据（原文：causes Fiddler to automatically respond to HTTP/401 and HTTP/407 challenges that use NTLM or Negotiate protocols using the current user's Windows credentials.）

UI 选项：点击里面的“tear off”按钮，会把Composer作为一个独立的窗口运行。

### 2 最后

以上就是使用fiddler发送请求的介绍了。后续再介绍fiddler修改请求吧~

---

Now：2018年8月8日02:29:18
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=481519556&auto=1&height=66"></iframe>
