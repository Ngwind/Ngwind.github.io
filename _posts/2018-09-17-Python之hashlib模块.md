---
layout: post
title: Python之hashlib模块
tags:
  - python
date: 2018-09-17 15:06:02
---

### hashlib介绍

Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串 `how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
<!-- more -->
### 使用hashlib

通过hashlib.hash函数名（）来获得一个hash对象。比如获得一个md5hash函数对象：

```python
m = hashlib.md5()
```

#### hash对象的方法

hash对象有四个常用的方法：
 - update（arg)
 - digest()
 - hexdigest()
 - copy()

##### update方法

update(arg)方法使用arg中的字节来更新hash对象。arg参数要指明编码格式,否则报错。

注意：如果多次调用同一个hash对象的update方法。相当于多个arg拼接在一起。（后面会有演示）

```python
m.update("wuwenda".encode("utf-8"))
```

##### digest方法

digest()返回加密后的密文（准确说是摘要信息）
```python
dig = m.digest()
print(dig)
```
运行结果：
```
b'*?\xc1\xe1w\xa1\xe9g\x1d\x1d\x10\x83t}u\xad'
```

##### hexdigest方法

hexdigest()方法和digest方法类似的,只不过返回的密文是作为双倍长度的unicode对象返回的，只包含十六进制字符。

```python
dig = m.digest()
print(dig)
print(type(dig))
hdig = m.hexdigest()
print(hdig)
print(type(hdig))
```
运行结果：
```
b'*?\xc1\xe1w\xa1\xe9g\x1d\x1d\x10\x83t}u\xad'
<class 'bytes'>
2a3fc1e177a1e9671d1d1083747d75ad
<class 'str'>
```
可以看出，digest方法返回的是bytes对象，hexdigest方法返回的是str对象。

##### copy方法

copy()方法返回hash对象的副本.这个功能主要用来提升代码性能，如果有子字符串多次被使用，则可以使用copy方法直接，避免重复的hash计算。

#### 同一hash对象多次使用update(arg)

注意看下面两种方法，它们生成的摘要都是相同的。希望可以通过这个例子，来明白多次调用的情况。

1. 使用一次update
  
   ```python
   m1 = hashlib.md5()
   m1.update("wuwenda123".encode("utf-8"))   
   print(m1.hexdigest())
   ```

   输出为：

   ```
   a06c86d9a4df8de61c90af9bfd7572c9
   ```

2. 使用两次update
   ```python
   m2 =hashlib.md5()
   m2.update("wuwenda".encode("utf-8"))
   m2.update("123".encode("utf-8"))
   print(m2.hexdigest())
   ```

   输出为：

   ```
   a06c86d9a4df8de61c90af9bfd7572c9
   ```

多次调用update()就相当于把多个arg参数拼接
