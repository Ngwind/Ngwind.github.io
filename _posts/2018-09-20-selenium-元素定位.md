---
layout: post
title: selenium-元素定位
tags:
  - selenium
date: 2018-09-20 11:17:44
---

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=298 height=52 src="//music.163.com/outchain/player?type=2&id=423226&auto=0&height=32"></iframe>

## 元素定位方法

上一节我们已经配置好了环境并且可以通过脚本打开浏览器了，说明我们已经打开了自动化测试的大门，接下来就开始学习如何定位页面元素。

html页面是由一个个的标签组成的，我们定位元素其实就是定位这些标签。selenium提供了8种查找定位元素的方法：

- ID
- name
- Xpath
- link test
- partial link test
- tag name
- Class name
- CSS selector  

>最好的学习方法还是去源码！这写方法的使用方式，在源码注释中都有说明。
>
>在selenium包->webdriver文件夹->remote文件夹->webdriver.py

为了方便演示，创建一个thml文件，文件内容如下：
```Html
<html>

<body>
  <p class="content">Site content goes here.</p>
  <form id="loginForm">
    <input name="username" type="text" />
    <input name="password" type="password" />
    <input name="continue" type="submit" value="Login" />
    <input name="continue" type="button" value="Clear" />
  </form>
  <div>
    <p>Are you sure you want to do this?</p>
    <a href="continue.html">Continue</a>
    <a href="cancel.html">Cancel</a>
  </div>
</body>
<html>
```

提前介绍一下,这些函数都是通过webdriver对象来调用的，所以我们要先获得一个webdriver对象：

```python
driver = webdriver.Chrome()
driver.get("file://C:/Users/Administrator/Desktop/learn-selenium.html")  
```

## 通过ID查找元素

对于属性有id的元素（标签），我们可用通过id查找元素。函数为`find_element_by_id(arg)`.这个方法会返回页面中第一个被匹配的元素对象。如果找不到任何元素，则抛出NoSuchElementException异常

例如，可以通过下面的方式定位到from元素：

```python
elem_form = driver.find_element_by_id("loginForm")
```

## 通过name查找元素

对于属性有name的元素（标签），我们可用通过name查找元素。函数为`find_element_by_name(arg)`.这个方法会返回页面中第一个被匹配的元素对象。如果找不到任何元素，则抛出NoSuchElementException异常

例如，可以通过下面的方式定位元素：
```python
elem_username = driver.find_element_by_name("username")
elem_password = driver.find_element_by_name("password")
```

## 通过Xpath查找元素

XPath是XML文档中查找结点的语法。因为HTML文档也可以被转换成XML(XHTML)文档， Selenium的用户可以利用这种强大的语言在web应用中查找元素。 XPath扩展了（当然也支持）这种通过id或name属性获取元素的简单方式，同时也开辟了各种新的可能性， 例如获取页面上的第三个复选框。

使用XPath的主要原因之一就是当你想获取一个既没有id属性也没有name属性的元素时， 你可以通过XPath使用元素的绝对位置来获取他（这是不推荐的），或相对于有一个id或name属性的元素 （理论上的父元素）的来获取你想要的元素。XPath定位器也可以通过非id和name属性查找元素。

绝对的XPath是所有元素都从根元素的位置（HTML）开始定位，只要应用中有轻微的调整，会就导致你的定位失败。 但是通过就近的包含id或者name属性的元素出发定位你的元素，这样相对关系就很靠谱， 因为这种位置关系很少改变，所以可以使你的测试更加强大。

函数为`find_element_by_xpath(arg)`.arg为xpath表达式。

例如，通过下面方式定位元素：
```python
clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
elem_p = driver.find_element_by_xpath("//p")
```
通过xpath查找定位的方式很强大，不过要用好xpath定位，还需要进一步掌握xpath的语法。

>学习xpath定位:https://www.jianshu.com/p/89c10770d72c

## 通过link text查找元素

当你知道在一个锚标签中使用的链接文本时，可以使用链接文本定位。页面中第一个匹配链接内容锚标签会被匹配并返回。如果找不到任何元素，会抛出`NoSuchElementException`异常。

使用`find_element_by_link_text(arg)`,返回链接文本匹配arg的标签。此外，也可以使用`find_element_by_partial_link_text(arg)`,返回链接文本包含arg的标签。

例如，通过下面方式定位元素：
```python
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')
```

## 通过tag name查找元素

如果你想通过标签名来定位元素，可以使用函数`find_element_by_tag_name(arg)`.不过这个方法定位不是很好用，毕竟页面中的同tag有很多个嘛.同样，如果找不到任何元素，会抛出`NoSuchElementException`异常。

例如，通过下面方式定位元素：

```python
elem_form_tag = driver.find_element_by_tag_name("form")     
```

## 通过class name查找元素

对于属性有class的元素（标签），我们可用通过class查找元素。函数为`find_element_by_class_name(arg)`.这个方法会返回页面中第一个被匹配的元素对象。如果找不到任何元素，则抛出NoSuchElementException异常。

例如，通过下面方式定位元素：

```python
elem_content = driver.find_element_by_class_name("content")    
```

但是，在实际情况下有些元素会有多个class，这时候不能定位成功，一般较少用classname进行定位查找。

## 通过css选择器查找元素

通过css selector来查找也是一种强大的方法，它和xpath不相上下。函数为`find_element_by_css_selector(arg)`.这个方法会返回页面中第一个被匹配的元素对象。如果找不到任何元素，则抛出NoSuchElementException异常。

例如，通过下面方式定位元素：
```python
elem_continue_css = driver.find_element_by_css_selector("p.content")
```

## 用elements查找多个

webdriver中还有一类函数，它和find_element_by类似，不过这类函数不是返回单个匹配的元素，而是返回所有匹配的元素组成的列表。只要把element改成elements就可以了。例如：`find_elements_by_xpath()`、`find_elements_by_id()`等等。

## 通用的查找方法

可以使用webdriver的`find_element(by,arg)`函数。By类中可以选择定位的方法（上面提到的8种），arg为匹配的字符串。不过，官方文档中建议我们优先使用上面的具体定位方法。

此外，也有`find_elements(by,arg)`函数，返回所有匹配元素组成的列表。

## 总结

定位元素是web自动化的重要基础，需要熟练掌握，多多练习。定位元素的方法有很多，特别要掌握xpath或css selector这两种强大的定位方式。认真学习xpath的语法吧!

