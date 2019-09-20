---
layout: post
title: Pytest（五）了解内置fixtures
date: 2019-09-19 14:11:44
categories: 
  - pytest  
tags: 
  - pytest
  - python
---

pytest内置了一些通用的fixutre，称之为内置fixtures。

内置fixture可以帮助我们方便地处理一些非常有用的事情。例如，提供临时文件目录、访问命令行选项、测试session之间通信、验证输出流、修改环境变量等
<!-- more -->

## 使用tmpdir和tmpdir_factory

`tmpdir`和`tmpdir_factory`这两个fixtures用于在测试运行之前创建临时文件目录，并在测试完成后删除目录。如果要测试文件的读、写或者修改的时候，可以使用`tmpdir`来给每个测试用例创建一个临时的文件目录。如果想让多个测试用例共用一个临时目录，则可以使用`tmpdir_factory`。

`tmpdir`的scope是function，`tmpdir_factory`的scope是session。

```python
def test_needfiles(tmpdir):
    print(tmpdir)  # 会打印tmpdir路径，因为tmpdir实现了__str__方法
    assert 0

```

tmpdir这个fixturn会`return`一个`py.path.local`对象。这个对象相当于是对`pathlib.Path`的封装（自从python3.4后，推荐使用`pathlib`代替`os.path`）。

> 关于py.path.loacl对象的api参考[这里](https://py.readthedocs.io/en/latest/path.html#reference-documentation)
> 
> pathlib和os.path的对比参考[这里](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module) 

临时目录的前缀路径是可以修改的。使用`pytest --basetemp=/path/you/want`就可以指定临时目录的前缀路径。

### 在其他域使用临时目录

我们可以使用`tmpdir`和`tmpdir_factory`分别创建function域和session域的临时目录，但是有个问题是：假如我们想要module域的临时目录，要怎么创建呢？(**想象一下，一个module中的所有test函数都要共用一个临时目录中的json文件**)))

答案是：自定义一个`module`域的`fixture`，这个`fixture`使用`tmpdir_factory`来获取一个session级别的临时目录，然后`fixture`return一个新的临时目录。

```python
import json
import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file_ = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file_)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file
```

module中的所有使用了上面的fixture的测试函数，都共用一个临时目录。

## 使用pytestconfig

pytest有一个内置`fixture`叫做`pytestconfig`。这个fixture是于pytest的配置参数相关的。
`pytestconfig`这个`fixture`返回一个`_pytest.config.Config`对象。可以调用该对象的属性和方法获取相关配置信息。

## 使用cache

pytest有个内置`fixture`叫做`cache`。这个fixutre是和缓存相关的。可以将一次session的结果保存，然后下一次session运行时，可以获取缓存信息。

使用`pytest --cache-show`可以列出上次测试的结果。
使用`pytest -lf`可以列出上次失败的测试用例。
使用`pytest -ff`可以优先执行上次失败的测试用例。
使用`pytest --clear--cache`可以清除缓存。

此外，如果测试函数使用了`cache`这个内建`fixture`，可以调用`cache.get(key,default)`和`cache.set(key,value)`来保存和获取数据到缓存中。

> 还有其他内置的fixture。等于要用到了，再进一步了解。