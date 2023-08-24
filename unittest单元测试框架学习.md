# unittest单元测试框架学习

记录时间2023-08-23  pm23：37

## 单元测试框架有哪些

### 简介

单元测试：指的是在软件开发 中，对程序的最小 单元（函数，方法）进行测试的过程

unittest不仅仅用于单元测试，还可以用于自动化测试用例的开发和执行，组织执行自动化测试用例。并且提供一些丰富的断言方法，判断用例是否通过，最终能够生成测试报告

### 基于python的单元测试框架有哪些？

unittest:更简单，容易上手

pytest：市场份额更多，是上面的升级版本。

一般情况下，能用Pytest尽量用Pytest。如果团队的编码能力不强就用Unittest。

web自动化选择unittest，接口自动化用pytest

可以选择全部掌握。

### 默认测试用例的规则差异

unittest:

新建一个类，必须继承unittest.TestCase(耦合)

导入unittest模块（ALT+ENTER)

测试用例必须以test_开头

Pytest：

测试文件必须以test_开头或者_  _test结尾（非耦合）

测试类名必须Test开头

测试用例必须以test_开头。

所有的开发：都遵循非耦合的开发方式，Spring,前后端分离的架构



2夹具的差异

unittest：

setUp/tearDown   在每个用例的前后执行

setUpClass/tearDownClass  在每个 类的前后执行

setUpModule/tearDownModule 在每个模块的前后执行

pytest:

setup/teardown   在每个用例的前后执行

setup_class/teardown_class  在每个 类的前后执行

setup_module/teardown_module 在每个模块的前后执行



3.断言的差异

unittest:self.assertEqual()

pytest:        python原生的assert

4.失败用例重跑的差异

unittest 没有这个功能

pytest:支持

5.参数化的差异

unittest: ddt

pytest:   @pytest.mark.parametrize()   

三单元测试框架的作用

1.找到测试用例，根据他们默认的测试用例规则（知道它的原理、底层，）

2.执行用例

3.判断测试用例的结果

4.生成测试报告 

四.unittest重要组件

TestCase测试用例;

TestSuite测试套件:整理测试用例，形成一个集合

TestFixture测试固件：就是上面的夹具。

TestLoader测试加载器：加载测试用例套件或测试用例

TestRunner测试运行器：运行测试用例

五  unittest如何运行测试用例

初学者方法

​	

```python
import unittest
class TestApi(unittest.TestCase):
    def test_mashang(self):
        print("this is a beaging")

if __name__ == '__main__':
    unittest.main()
```

unittest的运行方式有两种：

1、命令行的运行方式(unittest默认的执行方式)

直接在命令行中(terminal)中运行

`python -m unittest test_api.py`

`python -m unittest test_api.TestApi.test_baili`

第二个直接执行文件中的某个测试用例

另外根据光标的位置的不同，执行用例的数量也有区别。如果是放在类旁边，就是执行这个类下的所有用例。如果是在某个用例旁边就是执行单一这个用例。

果然是学习才是最快的方法

python -m就是以命令行的方式运行测试用例

unittest -v 就是以更详细的方式展示测试结果

`python -m unittest -v test_api.py`

-k 根据通配符的方式查找指定的用例执行

`python -m unittest -v test_api.py -k *_baili`

2.mian方式运行

