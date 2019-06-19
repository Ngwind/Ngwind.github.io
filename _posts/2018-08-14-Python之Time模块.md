---
layout: post
title: Python之Time模块
tags:
  - python
date: 2018-08-14 23:22:07
---
## 0 前言

最近抽空学习了Python的Time模块。time模块主要用来获取和处理时间相关的数据。这个模块还是比较简单易懂的。接下来介绍一下time模块的主要函数。
<!-- more -->
## 1 Time介绍

首先，time模块中用到的时间数据类型有3类：时间戳、时间元组、时间字符串。
- 时间戳是float型数据，表示从1970年1月1日到某个时间点的总计秒数。
- 时间元组是time模块中定义的tuple类型数据。主要有9部分：
  - m_year 年
  - tm_mon 月
  - tm_mday 日
  - tm_hour 小时
  - tm_min 分钟
  - tm_sec 秒钟
  - tm_wday 星期
  - tm_yday 月份
  - tm_isdst 是否夏令时
  
  官方文档中这样介绍：
  ```python
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
  ```
- 时间字符串是string类型的数据，一种便于阅读的时间数据表示形式。
  
## 2 主要函数

#### time()

time函数返回当前时间戳

示例：
```python
t1 = time.time()  # time函数返回当前时间戳-float型数据
print("time函数返回当前时间戳-float型数据")
print(t1)
print(type(t1), "\n")
```
输出：
```python
time函数返回当前时间戳-float型数据
1534260500.7620687
<class 'float'> 
```

#### localtime(secs)

localtime函数可以接收一个时间戳，返回一个时间元组；如果参数为空，则返回当前时间的元组。

示例：
```python
t2 = time.localtime(1493890956)  # localtime函数接受一个时间戳，返回一个时间元组
print("localtime函数接受一个时间戳，返回一个时间元组")
print(t2)
print(type(t2), "\n")
```
输出
```python
localtime函数接受一个时间戳，返回一个时间元组
time.struct_time(tm_year=2017, tm_mon=5, tm_mday=4, tm_hour=17, tm_min=42, tm_sec=36, tm_wday=3, tm_yday=124, tm_isdst=0)
<class 'time.struct_time'> 
```

#### asctime(t)

asctime函数接受一个时间元组，返回一个格式化的字符串

示例：
```python
t3 = time.asctime(t2)  # asctime函数接受一个时间元组，返回一个格式化的字符串
print("asctime函数接受一个时间元组，返回一个格式化的字符串")
print(t3)
print(type(t3), "\n")
```
输出：
```python
asctime函数接受一个时间元组，返回一个格式化的字符串
Thu May  4 17:42:36 2017
<class 'str'> 
```

#### ctime(secs)

ctime函数相当于localtime+asctime的结合

示例：
```python
t4 = time.ctime(t1)  # ctime函数相当于localtime+asctime的结合
print("ctime函数相当于localtime+asctime的结合")
print(t4)
print(type(t4), "\n")
```
输出：
```python
ctime函数相当于localtime+asctime的结合
Tue Aug 14 23:28:20 2018
<class 'str'> 
```
#### strftime(format,t)

strftime函数将时间元组转换成格式化时间字符串

示例：
```python
t5_1 = time.strftime('%Y-%m-%d %H:%M:%S %a %b', t2)  # strftime函数将时间元组转换成格式化时间字符串
t5_2 = time.strftime('%A %B %p %I:%M:%S %z')
print("strftime函数将时间元组转换成格式化时间字符串")
print(t5_1)
print(t5_2, '\n')

```
输出：
```python
strftime函数将时间元组转换成格式化时间字符串
2017-05-04 17:42:36 Thu May
Tuesday August PM 11:28:20 +0800 
```
#### strptime(str,format)

strptime函数将字符串解析，输出时间元组

示例：
```python
t6 = time.strptime('2018年8月14日10点3分45秒', '%Y年%m月%d日%H点%M分%S秒')  # strptime函数将字符串解析，输出时间元组
print("strptime函数将字符串解析，输出时间元组")
print(t6)
print(type(t6), "\n")
```
输出：
```python
strptime函数将字符串解析，输出时间元组
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=14, tm_hour=10, tm_min=3, tm_sec=45, tm_wday=1, tm_yday=226, tm_isdst=-1)
<class 'time.struct_time'> 
```
#### gmtime(secs)

gmtime函数接收时间戳输出格林尼治时间元组

示例：
```python
t7 = time.gmtime(t1)  # gmtime函数接收时间戳输出格林尼治时间元组
print("mgtime函数接收时间戳输出格林尼治时间元组，注意loacltime()是输出本地区的时间元组")
print(t7)
print(type(t7), "\n")
```
输出：
```python
gmtime函数接收时间戳输出格林尼治时间元组，注意loacltime()是输出本地区的时间元组
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=14, tm_hour=15, tm_min=28, tm_sec=20, tm_wday=1, tm_yday=226, tm_isdst=0)
<class 'time.struct_time'> 
```
#### mktime(t)

mktime函数与gmtime函数相反，接收一个时间元组输出时间戳

示例：
```python
t8 = time.mktime(t7)  # mktime函数与gmtime函数相反，接收一个时间元组输出时间戳
print("mktime函数与gmtime函数相反，接收一个时间元组输出时间戳")
print(t8)
print(type(t8), "\n")
```
输出：
```python
mktime函数与gmtime函数相反，接收一个时间元组输出时间戳
1534231700.0
<class 'float'> 

```
#### clock()

返回进程开始后的cpu运行时间

示例：
```python
t3 = time.asctime(t2)  # asctime函数接受一个时间元组，返回一个格式化的字符串
print("asctime函数接受一个时间元组，返回一个格式化的字符串")
print(t3)
print(type(t3), "\n")
```
输出：
```python
返回进程开始后的cpu运行时间
E:/PycharmProjects/practise_20180814/test_time.py:63: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
5.021518962
  t10 = time.clock()  # 返回进程开始后的cpu运行时间
<class 'float'> 
```

这里警告说clock函数将在3.8版本被抛弃，新版本建议使用pref_counter()和process_time().

#### sleep(secs)

推迟调用线程的运行，secs指秒数。

示例：
```python
t9 = time.sleep(5)  # 推迟调用线程的运行，secs指秒数。
print("推迟调用线程的运行，secs指秒数。")
print(t9)
print(type(t9), "\n")
```
输出：
```python
推迟调用线程的运行，secs指秒数。
None
<class 'NoneType'> 
```

## 3 最后
附上一个关系图：

![](/img/2018-08-20 093311.png)

time模块比较简单也是比较常用的模块，要搞清楚3种数据类型的转化。此外，还可以使用sleep（）来挂起线程。接下来会学习与time模块相关的模块calendar模块

---

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=503602561&auto=1&height=66"></iframe>
