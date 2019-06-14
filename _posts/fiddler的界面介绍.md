---
layout: post
title: 二、【fiddler】的界面与抓包
tags:
  - fiddler
date: 2018-07-30 18:00:48
---

### 0 前言

上一篇中介绍了fiddler的安装与配置，这一篇文章将对fiddler的界面进行介绍。以及查看抓取的数据包。

---

### 1 开启抓取网络会话

在Fiddler中，勾选上File->Capture Traffic 或者在左下角点击Capturing，就可以开始抓包啦！如果你要抓取https协议包，记得做好相关的配置，具体可以查看上一篇文章。

第一种方法
![](/img/2018-07-31 095221.png)

第二种方法
![](/img/2018-07-31 095331.png)

如果完成了上述操作，还不能抓到包，可能是你其他地方没有设置好，可以检查浏览器是否启用了代理、在filter中查看是否启用了过滤器（我自己演示的时候，就是忘了关掉过滤器导致半天都没抓到包...）等

![](/img/2018-07-31 095701.jpg)

如果你操作正常，应该就可以在会话列表中看到数据包了：

![](/img/2018-07-31 095857.jpg)

### 2 查看网络会话

#### 2.1 查看网络会话详细信息

在会话列表中，以表格的形式给我们展现了所有抓到的数据包，展示的信息有：id号、响应码、协议名、域名、数据格式、url、传输数据大小、缓存类型、进程、备注等。这些表头可以通过拖动来自定义顺序和行宽。

![](/img/2018-07-31 100542.jpg)

#### 2.1 查看网络会话统计信息

我们可以在Statistics中查看网络会话的信息统计（主要是对时间、空间的统计）：

1. 在会话列表点击选中1或多个会话
2. 在右边点击Statistics 
  
![](/img/2018-07-31 100928.png)

#### 2.2 分析网络会话

我们可以在Inspectors中查看网络会话的数据内容,inspectors中的信息是我们工作中查看的主要内容。

1. 点击选中一个会话
2. 点击右边的Inspectors
   
![](/img/2018-07-31 101557.jpg)

我们看看界面的右边，上半部分是请求request的信息，可以查看请求头header、请求主体textview、表单webforms、cookies、json格式查看等。下半部分是响应response的信息，可以查看响应头、响应主体、以图片、网页、json、xml、raw等格式查看响应的消息内容。

#### 2.3 查看网络会话的传输耗时

使用Timeline查看1或者多个会话的传输耗时

1. 在会话列表选中1或多个会话
2. 点击右边的Timeline栏
  
![](/img/2018-07-31 102524.jpg)

### 3 查找与过滤会话

#### 3.1 查找会话

有时候，抓到的数据包太多，在这么多会话中找到我们要分析的那个是比较麻烦的。fiddler给我们提供了一个find功能，用来搜索特定的会话。

##### 3.1.1 使用find选项框

点击find会弹出一个对话框，我们可以在find文本框中输入要搜索的文本。下方的options中可以进行高级设置。找到符合条件的会话，会通过高亮的方式标记显示。

![](/img/2018-07-31 104439.png)

##### 3.1.2 使用命令行QuickExec

fiddler提供了一个命令行工具，后面会专门学习命令行的使用。我们可以使用命令行来查找特定会话。
命令行是在左下角的一个黑框。输入`?sometext`即可搜索和'sometext'相关的会话。

![](/img/2018-07-31 105420.png)

#### 3.2 过滤会话

除了用find，还有一种方便我们查看会话的方法，就是使用过滤filter功能。在右侧菜单中，找到Fittlers选项，共有9个部分进行设置。

![](/img/2018-07-31 105841.png)

1. Use Filters：勾选则表示使用过滤，不勾选则表示不进行过滤
2. Actions：有四个选项，Run Filterset now：立即运行过滤设置；Load Filterset：加载保存的过滤设置；Save Filterset：保存过滤设置；help：帮助
3.  Hosts：该设置项有两个选项
   - 第一个下拉框是只显示内网或者外网选项
  ![](/img/2018-07-31 110028.png)
   - 第二个下拉框是根据主机名信息显示或者隐藏或者标记指定请求
  ![](/img/2018-07-31 110124.png)
4. Client Process：有三个选项，Show only traffic from：根据进程信息进行过滤，选择后，将只显示由该进程发出的请求；Show only Internet Explorer traffic：只关心由IE浏览器发出的请求；Hide traffic from Service Host：隐藏来自service host（即由svchost.exe进程发出）的请求
5. Request Headers：有五个选项，Show only if URL contains：可以通过正则表达式过滤请求地址中包含或不包含的内容，例如REGEX:\.(js|css|js\?.*|css\?.*)$（隐藏所有js和css请求）；Hide if URL contains：与Show only if URL contains相反，一个是显示，一个是隐藏；Flags requests with headers：支持指定某个http请求头名称，如果在web session列表中存在该请求头，会加粗显示该session；Delete requests headers：与Flags requests with headers类似，这里是如果包含该请求头，则删除该请求头；Set request header：将HTTP请求头更新为所输入的值。
6. Breakpoints：断点设置，有四个选项。Break request on POST：对POST请求设置断点；Break request on GET with query string：会为所有方法为GET且URL中包含了给定查询条件的请求设置断点；Break on XMLHttpRequest：对所有能够确定是通过XMLHTTPRequest对象发送的请求设置断点；Break response on Content-Type：会为所有响应头Content-Type中包含了指定文本的响应设置响应断点。
7. Response Status Code：根据响应状态码设置断点。
8. Response Type and Size：有几种类型，一类是根据响应数据的类型显示或隐藏；一类是根据响应数据的大小显示或隐藏；一类是根据响应所需要的时间设置背景颜色；一类是根据文件类型进行限制。
   - type有以下几种类型：
  ![](/img/2018-07-31 110304.png)
   - Time HeatMap复选框会基于服务器返回给定响应所需要的时间为每个session设置背景颜色。
9. Response Headers：与Request Headers不同的是，这块区域是针对响应数据的头部进行过滤。

这么多设置项，比较常用的就是1.2.3部分。通过过滤设置，可以快速的帮助我们找到我们需要抓包分析的数据包，从而提高效率，避免过多的数据包信息干扰我们找到正确的数据包。

#### 3.3 比较两个会话

选中会话list中的多个会话，然后右键点击，选择comprare。

![](/img/2018-07-31 112249.png)

可能你点击compare之后会弹出错误提示框，别慌，往下看：

##### 3.3.1 安装插件来比较会话

默认情况下，fiddler尝试打开windiff或者winmerge来比较两个会话，不过默认没有安装这些插件，需要我们自行下载...我没有使用这些插件。如果需要，可以点击参考[这个](https://support.microsoft.com/zh-cn/help/159214/how-to-use-the-windiff-exe-utility)文档进行下载安装。

##### 3.3.2 更改默认文本比较工具

如果你电脑有一些比较高级的编辑器，可以使用这些编辑器来来比较两个会话。不过使用之前，我们要改变fiddler默认的文本比较工具。

1. 点击Tools->Fiddler Options->Tools
2. 找到你编辑器的程序路径即可。

![](/img/2018-07-31 112504.png)

### 3 其他

使用fiddler查看网络数据包就先介绍到这里，欢迎补充！下一篇我们将学习如何截获并且修改网络请求和响应~