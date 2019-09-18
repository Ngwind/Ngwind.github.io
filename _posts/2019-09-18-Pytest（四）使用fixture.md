---
layout: post
title: Pytest（四）使用fixture
date: 2019-09-18 15:07:32
categories: 
  - pytest  
tags: 
  - pytest
  - python  
---

pytest的fixtures是使pytest在其他测试框架之上脱颖而出的独特核心功能之一，也是许多人使用pytest的原因。在pytest中，fixture指的是一种分离出“测试准备工作”和“测试结束收尾工作的代码的机制。
<!-- more -->

## 创建fixture

给函数增加一个`@pytest.fixture()`装饰器，pytest就会把该函数作为一个`fixture`。如果测试函数的形参中填写了fixture，pytest就会在测试函数运行之前调用这些fixtures。fixture可以用来执行通用的工作，也可以return数据给测试函数。

```python
import pytest

@pytest.fixture()
def func():
    return 1

def test_func(func):
    assert func == 0
```

如上，`test_func`函数形参中传入了名为`func`的`fixture`。pytest会在`module`中查找名为func的函数。如果在module中找不到fixture，还会在`conftest.py`中寻找。

## 通过confest.py共享fixtures

我们可以把fixture放在独立的文件中。但是，想要让所有的测试函数都能使用`conftest.py`中的fixtures，则需要把文件放在所有测试函数文件的最上层目录。

尽管conftest.py是一个`module`，但是不要手动`import`它。它会被pytest自动识别并当作一个本地`plugin`。（关于插件的内容后面进一步学习）目前，只要把conftest.py想象成一个使得我们可以在目录下放置所有测试函数使用的`fixture`的地方即可。

## 用fixture实现setup和teardown功能

许多测试用例都有`setup`和`teardown`的部分，即测试环境准备和环境清理。通过在fixture中使用`yield`关键字，可以很方便的实现setup和teardown。

```python
import pytest

@pytest.fixture()
def fixture_func():
    print("start")
    yield
    print("end")


def test_func(fixture_func):
    assert 1

```

yield前面的部分，是setup部分，会在测试函数前运行。yield后面的部分，是teardown部分，会在测试函数后运行。

### 使用--step-show跟踪fixture执行

在运行pytest时，添加`--setup-show`选项后，能够在输出中观看到fixture执行过程。

```shell
>pytest --setup-show test_fixture.py

=================================== test session starts ====================================
platform win32 -- Python 3.7.0, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
rootdir: E:\pytestLearning\pytest-Learning
collected 1 item                                                                            

test_fixture.py
        SETUP    F fixture_func
        test_fixture.py::test_func (fixtures used: fixture_func).
        TEARDOWN F fixture_func

==================================== 1 passed in 0.04s =====================================
```

如上，显示了fixtures的调用过程。
`SETUP`和`TAEADOWN`调用了`fixture_func。
`S`表示`session`域的fixture、`M`表示`module`域的fixture、`F`表示`function`域的fixture、`C`表示`class`域的fixture。

## 使用fixture提供测试数据

fixture很适合用来提供测试数据。fixture可以`return`任何数据类型。测试函数使用fixture函数名就能使用`return`的数据。

```python
import pytest

@pytest.fixture()
def func1():
    return 1

def test_func(func1):
    assert func1 == 1  # func1的值为1，断言通过

```
## fixture的嵌套

fixture函数的入参也可以填写fixture`，这出现了嵌套调用fixture的情况。

```python
import pytest

@pytest.fixture()
def func1():
    print("func1")

@pytest.fixture()  # func2:[func1]
def func2(func1):
    print("func2")
    return "func2"

@pytest.fixture()  # func3:[func2]
def func3(func2):
    print("func3")
    return "func3"

def test_func(func2, func3): # test_func:[func2,func3]
    assert func2 == "hello"

```

运行结果：

```shell
>pytest --setup-show test_fixture.py

test_fixture.py::test_func
        SETUP    F func1
        SETUP    F func2 (fixtures used: func1)
        SETUP    F func3 (fixtures used: func2)
        test_fixture.py::test_func (fixtures used: func1, func2, func3)FAILED
        TEARDOWN F func3
        TEARDOWN F func2
        TEARDOWN F func1

========================================= FAILURES =========================================
________________________________________ test_func _________________________________________

func2 = 'func2', func3 = 'func3'

    def test_func(func2, func3):
>       assert func2 == "hello"
E       AssertionError: assert 'func2' == 'hello'
E         - func2
E         + hello

test_fixture.py:24: AssertionError
```

## 指定fixture的域

pytest.fixture()有个参数叫做`scope`，用来控制fixture的作用级别。scope可选值为：

- `function`：作用于每个函数。setup部分在每个函数前运行，teardown部分在每个函数后运行。scope默认为function。
- `class`：作用于每个类。无论类中有多少个函数声明了该fixture，只运行一次。
- `module`：作用于每个模块。无论一个模块中有多少个函数或方法声明了该fixture，只运行一次。
- `session`：作用一次会话（pytest任务）。在一次pytest任务中，该fixture只在启动和结束时运行一次。

## 通过pytest.mark.usefixtures指定fixtures

通过前文，我们了解到，要使用fixtures，可以把fixture函数名写到函数的入参中。不过，还有另一种方法可以使用fixture。

```python
import pytest


@pytest.fixture()
def fix_func1():
    print("setup1")
    yield
    print("teardown1")


@pytest.fixture()
def fix_func2():
    print("setup2")
    yield
    print("teardown2")


@pytest.mark.usefixtures("fix_func1", "fix_func2")
class TestClass1():

    def test_func1(self):
        assert 1

    def test_func2(self):
        assert 1 == 1

```

使用`@pytest.mark.usefixtures()`装饰器也可以给函数指定fixture。注意，`usefixtures()`函数里面填的不是**函数名**，而是**函数名字符串**。使用`usefixtures()`和直接在形参中填写fixtures的方式没有区别。但是，使用usefixtures()方式，测试函数不能获取fixture函数的`return`值。

当我们要给一个测试class中的所有测试方法使用相同的fixture，且不需要fixture的return值的时候，可以用`@pytest.mark.usefixtures()`。

## 通过autouse参数让测试函数默认使用fixture

`pytest.fixture()`有个`autouse`参数。这个参数决定一个fixture是否是默认被使用的。设置`autouse=True`则fixture默认被所有测试函数使用。`autouse`默认值为`False`。

```python 
import pytest


@pytest.fixture(autouse=True)
def fix_func1():
    return 1


def test_func1():
    assert 1 == fix_func1  # fix_func1 == <function fix_func1 at 0x0000024E5272C378>

```

使用pytest --setup-show 查看函数执行，发现`SETUP`和`TEARDOWN`都有fix_func1，但是断言是失败的，因为fix_func1的值不是1，而是一个函数对象。可能这是因为没有在test_func1函数的形参里定义fix_func1。

## 重命名fixture

pytest.fixture()有个`name`参数，可以让我们重命名fixture。

```python
import pytest


@pytest.fixture(name="new_fix_func")
def fix_func():
    return 1


def test_func(new_fix_func):
    assert new_fix_func == 1  # assert pass

```

## 参数化fixture