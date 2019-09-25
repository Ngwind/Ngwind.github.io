---
layout: post
title: Python之requests模块
date: 2019-09-25 11:41:17
categories: 
  
tags: 
  - python 
---


<!-- more -->

# Requests库

## import requests

通过查看源码，可以发现，当我们import了requests后， requests会再去import很多方法和属性。

from . import utils

from . import packages

from .models import Request, Response, PreparedRequest

from .api import request, get, head, post, patch, put, delete, options

from .sessions import session, Session

from .status_codes import codes

from .exceptions import (    RequestException, Timeout, URLRequired,    TooManyRedirects, HTTPError, ConnectionError,    FileModeWarning, ConnectTimeout, ReadTimeout)

## 请求

通过session.Session()获得一个request对象，进而通过调用request对象的方法，发送请求。

###  requests.request(method, url, params, data, json, headers, cookies, files, auth, timeout, allow_redirects, proxies, stream, verify, cert)

通用请求方法。其他具体请求方法（get()、post ()等）本质上是调用这个方法。返回一个Repsonse对象

- method

  http请求方法的字符串

- url

  要请求的url地址

- params

  （可选）传入一个字典。用于提供get方法的url参数

- data

  （可选）用于POST方法的请求pody：
  1.传入字典或二元组列表，作为HTML表单。
  2.传入字符串，直接发送字符串数据。

- json

  （可选）传入一个字典。可以直接转换成json字符串。自动添加请求头'Content-Type': 'application/json'

- headers

  （可选）传入一个字典，设置http请求头

- cookies

  （可选）设置http请求的cookies
  可传入字典
  可传入cookieJar对象

- files

  （可选）实现http文件上传请求。传入一个特定格式的字典。可以进一步了解。

- auth

  （可选）用于http认证。传入二元组(username,password)或auth对象。

- timeout

  （可选）传入浮点型或者二元组(connect time,read time)设置http等待响应超时时间。单位为秒。

- allow_redirects

  （可选）传入一个布尔值，设置允许http重定向。默认为True。

- proxies

  （可选）设置http代理。参考http://cn.python-requests.org/zh_CN/latest/user/advanced.html#proxies

- stream

  （可选）传入一个布尔值，默认为False。如果设置为True，可以流式获取http响应。参考http://cn.python-requests.org/zh_CN/latest/user/advanced.html#body-content-workflow

- verify

  （可选）用于https证书验证

- cert

  （可选）设置https的ssl证书。

### requests.get()

### requests.post()

### requests.put()

### requests.delete()

### requests.options()

### requests.head()

### requests.patch()

## 响应

请求完成会获得一个Response对象。可以通过使用这个对象获得http响应的信息，还可以获得http请求的信息。

### 属性

- status_code

  int类型。http响应码

- reason

  string类型。http的响应状态（OK、Not Found等）

- headers

  字典类型。http响应头。

- url

  string类型。响应的最终URL

- history

  一个Response对象的list。存放所有重定向的历史响应内容。

- cookies

  cookieJar对象类型，类似字典。存放相应的cookies。

- elapsed

  datetime.timedelta对象。记录发送到响应到达需要的时间。

- encoding

  string类型。设置response.text的编码方式。

- raw

  以流式获取响应内容。使用raw属性需要在请求时设置stream=True。

- request

  响应对应的request。本质上是PreparedRequest对象。

	- method

	  http请求方法。

	- url

	  请求的url地址。

	- headers

	  http请求头的字典。

	- body

	  http请求的body字符串。

	- hooks

### 属性方法

- ok

  判断请求状态。如果响应码<400，则返回True。否则返回False。

- is_redirect

  返回布尔值，判断本次请求是否被重定向。

- is_permanent_redirect

  判断本次请求是否被永久重定向。

- content

  bytes类型。http响应的body。

- text

  string 类型。 经过encoding的content。request会使用chardet库，猜测encode方式。

- apparent_encoding

  string类型。request猜测的encode方式。

- links

  http响应头中的link。

- next

  如果存在重定向请求，则为重定向链中的下一个请求返回PreparedRequest对象。

### 方法

- json()

  将json格式的响应body解析成字典。可以传入json.loads函数中的参数，底层调用json.loads()。

- raise_for_status()

  判断响应码，如果不小于400，抛出HTTPError。

- iter_content(chunk_size, decode_unicode)
- iter_lines(chunk_size, decode_unicode, delimiter)
- close()

  释放http连接。执行后，无法通过raw流式获取响应body。该函数通常不用显示调用。

## 会话

使用一个Session实例对象，创建多个request请求。可以实现跨请求保持参数（headers、cookies等）。

### 设置默认参数

requests.Session()获得一个session对象。通过给对象的属性赋值，可以设置默认参数。

- headers
- auth
- proxies
- hooks
- params
- stream
- verify
- cert
- max_redirects
- cookies

### 发送请求

和直接发送request请求的方法相同。requests.request()函数，本质上就是调用Session对象中的方法。

- request()
- get()
- post()
- delete()
- options()
- head()
- patch()
- put()

### 其他的方法

- prepare_request(request)

  在正式发起请求前做一些准备工作。传入一个request对象。返回一个PreparedRequest对象。

- send(preparedrequest)

  正式发送请求。传入一个PreparedRequest对象。返回Response对象。

## 响应码

Requests附带了一个内置的状态码查询对象：requests.codes.xxx。

## 异常

requests库实现了一些http相关的异常类型。包括错误和警告。

### RequestException

- HTTPError
- ConnectionError

	- ProxyError
	- SSLError

- Timeout

	- ConnectTimeout
	- ReadTimeout

- URLRequired
- TooManyRedirects
- MissingSchema
- InvalidSchema
- InvalidURL
- InvalidHeader
- ChunkedEncodingError
- ContentDecodingError
- StreamConsumedError
- RetryError
- UnrewindableBodyError

### RequestsWarning

- FileModeWarning
- RequestsDependencyWarning


