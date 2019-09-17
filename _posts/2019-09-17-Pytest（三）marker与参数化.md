---
layout: post
title: Pytest（三）marker与参数化
date: 2019-09-17 09:49:34
categories: 
  - pytest  
tags: 
  - python
  - pytest
---

pytest能够给测试用例添加不同的标记（marker）。当我们只需要运行部分测试用例时，我们可以使用标记来过滤。
pytest还支持参数化功能。给一个测试用例传入多组参数，减少重复的测试代码。

## 使用mark给测试用例打标签

`pytest`提供了一个很cool的机制，使得我们可以给测试函数打标签（marker）。一个测试函数可以有多个marker，而且一个marker可以由于多个测试函数。

通过给测试函数添加一个装饰器`@pytest.mark.xxx`，其中`xxx`可以是自定义的tag名称（pytest有内置了一些marker）。然后，使用`pytest -m 'xxx'`就可以只运行含有xxx标签的测试函数了。

```python
import pytest
# 使用pytest -m 'smoke'执行测试时，只会运行test_func1()
@pytest.mark.smoke
def test_func1():
    assert 1==0

def test_func2(): 
    assert 1==2

```

也可以给class添加装饰器，class中的所有测试函数都归属于class的mark。

另外，`pytest -m`命令是可以指定多个marker的，还可以排除多个marker。例如：`pytest -m 'aaa and bbb and not ccc'`表示运行aaa和bbb标签并且非ccc标签的测试用例。这里使用了类似python的逻辑表达式。


## 测试函数的参数化

`pytest`的参数化功能，也是使用装饰器实现的。

通过给测试函数添加一个装饰器`@pytest.mark.parametrize(name,values,ids)`。
- name是一个字符串变量。如果要使用多个变量，每个变量使用逗号隔开，组成一个name字符串。
- values是一个list。保存多组参数化数据
- ids是一个用来手动指定每组参数id的list，当values是一个引用数据类型的list时，通常会使用ids来设置一一对应的id。
- 也可以使用pytest.param(value,id="xxx")，分别给每组参数设定id（当values无法映射到一个ids时）。

```python 
import pytest

values_list = [(1,2,3), (1,2,2), (2,2,2)]

@pytest.mark.parametrize('n1,n2,n3', values_list)  # ids是选填参数
def test_func(n1,n2,n3):
    assert (n1,n2,n3)==(1,2,3)
```

另外，也可以对class使用装饰器，来实现整个class级别的参数化。

可以通过pytest命令行，只运行parametrize中的其中一组例如：`pytest "test_file.py::Testclass::test_func[v1-v2-v3]"`。v1 v2 v3 即为parametrize()中想要单独运行一组的参数。
