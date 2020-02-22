### 高级特性
#### 切片
list或tuple中可以使用':'
```
  l[3:6]          #that is l[3] l[4] l[5]
  l[:6]           #that is l[0] to l[5]
  l[-1]           #the last one
  l[-2]           #the one before last one
  l[1:6:2]        #l[1] to l[5] 每两个取一，即l[1] l[3] l[5]
```
#### 迭代
python 的for循环可以使用 for in 作用于list,tuple,dict
```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for k in d:
...     print(k)
...
a
c
b
```
```
>>>for v in d.values():
...     pass
```
```
>>>for k, v in d.items():
...     pass
```
#### 列表生成式
生成list ［1-10] 可使用：
```
list(range(1,11))     #不包括11
```
```
[x * x for x in range(1, 11)]   #生成[1*1, 2*2, ... , 10*10]
[m + n for m in 'ABC' for n in 'XYZ']   #列出['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```
#### 生成器
python在生成list或tuple时，如果包含元素很多，可以不用一次全部生成，而是迭代到哪生成到哪。
有两种生产方法：
1. 直接在列表生成式中，将［］改为（）
```
l = [x * x for x in range(10000)]   #一次性生成
g = (x * x for x in range(10000))   #使用生成器generator
next(g)                             #单步迭代，一次输出一个元素，输出0
next(g)                             #输出1
...
...
next(g)                             #最后一次迭代会抛出StopIteration错误

for n in g:
    pass                            #也可以用for循环迭代generator
```
2. 使用关键字**yield**返回结果
```
#拿生成Fibonacci数列举例，首先是正常列表生成式写出的函数
def l_fib(x):
    n, a, b = 0, 0, 1
    while n < x:
      print(b)
      n += 1
      a, b = b, a + b
    return 'done'

#其次是生成器写的fib
def g_fib(x):
    n, a, b = 0, 0, 1
    while n < x:
      yield b
      n += 1
      a, b = b, a+b
    return 'done'

#g_fib需要这样使用
f = g_fib(6)
next(f)
for n in g_fib(6):                    #或者for迭代
  print(n)                            #但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
                                      #如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
```

#### 迭代器
可以被next()函数调用并不断返回下一个值的对象称为*迭代器*：*Iterator*
for循环可以迭代list，tuple，dict，set，str以及generator，这些可用for循环迭代的对象成为可迭代对象：*Iterable*

判断对象是否可迭代Iterable：
```
from collections import Iterable
isinstance([],m Iterable)             #返回True
```
判断对象是否是迭代器Iterator：
```
from collections import Iterator
isinstance(g, Iterator)               #返回True
```
Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

Python的for循环本质上就是通过不断调用next()函数实现的：
```
for x in [1, 2, 3, 4, 5]:
    pass
#等价于
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

```

### 函数式编程
#### 高阶函数
***map/reduce***

python中的函数可以作为函数的参数和返回值，能被赋值给一个变量。
```
f = abs(-10)              #f是10
f = abs                   #f是abs函数，可以用f(-10)
abs = 10                  #此时调用abs(-10)会报错，因为abs已经被改为值是10的变量
```

map()函数：接受两个参数，一个是函数，一个是Iterable（例如list）

map将函数依次作用在Iterable的每个元素上，把结果以Iterator形式返回。
```
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))     #将list中的数字转换为字符串，返回['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

reduce()函数：接受一个函数和一个序列，但接受的函数必须有两个参数
```
from functools import reduce
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```
***filter***

filter()函数即过滤筛选函数，接受一个函数和一个序列，函数的返回值是True或False，根据返回值的真假依次决定序列元素的去留。
```
#删除序列中的空字符
def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['a', '', 'b', ' ', None]))
#返回['a', 'b']
```
***sorted***

sorted()函数,即排序函数，接受一个序列，也可一带一个函数来表明排序条件。
```
sorted([36, 5, -12, 9, -21])                        #返回[-21, -12, 5, 9, 36]
sorted([36, 5, -12, 9, -21], key = abs)             #返回[5, 9, -12, -21, 36]
sorted([36, 5, -12, 9, -21], reverse=True)          
#key接受的函数先作用于前面的list或dict等，形成新的序列，然后再用sorted排序
```
#### 返回函数
返回函数即将一个函数名作为函数的返回值。
```
def lazy_sum(*args):
  def add():
    sum = 0
    for n in args:
      sum += n
    return sum
  return add
#调用lazy_sum()时，返回的不是求和结果，而是函数add（）
f = lazy_sum(1, 3, 5, 7)
#调用f时，才计算结果
f()                                                 #返回16


f1 = lazy_sum(1, 3, 5, 7)
f1 == f                                             #返回False, lazy_sum每次调用都返回新函数
```
当函数返回一个函数时，相关参数和变量都保存在返回的函数中，这种程序结构称为*闭包(Closure)*

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#### 匿名函数
用关键字***lambda***定义的函数，可以不用函数名，后续也不会重复使用，缩短程序结构。
```
def add(x, y):
  return x + y
#等价于
lambda x, y: x + y
```

#### 装饰器decorator
装饰器是一种特殊的返回函数。一般情况下，如果想在其他函数执行时记录时间或者log，又不想重新在原来函数内部增加东西破坏结构，
就需要用到装饰器。
```
#用法
@log
def some_func():
  pass
#some_func执行时就会相当于执行 some_func = log(some_func)
```
装饰器的写法见示例[decorator.py](./decorator.py) 

注意：functools模块下的@functools.wraps()函数是为了保证使用装饰器后，some_func()的__name__属性不会变成装饰器返回的函数的__name__。

#### 偏函数
functools.partial(), 接受两个参数，一个是正常函数，一个是正常函数中的一个参数值，它将正常函数中的一个参数值固定，形成新的函数返回。
```
import functools
max(5, 6, 7)                                            #返回最大7
max2 = functools.partial(max, 10)                         
max2(5, 6, 7)                                           #相当于max(10, 5, 6, 7), 最后返回10
```
### 面向对象
#### 继承和多态
封装、继承和多态是面向对象的三大特性。

多态：发生条件是1.子类继承父类，2.子类重写父类的一个方法，3.编写函数接受父类为参数，并使用父类的方法，4.使用函数时传入子类实例，
则函数执行的是子类的重写方法。

对静态语言如java c++来说必须严格按以上条件发生多态，必须有继承发生。而对动态语言如python，不一定传入父类的子类，只需传入对象有同名的方法就可以。

#### __slots__
python作为动态语言，允许在class生成实例后再动态对实例绑定属性。

如果不想类的实例在使用时被随便绑定属性,可以在类定义中用__slots__限定
之后该类实例能添加的属性。
```
class Students(object):
  __slots__ = ('name', 'age')                           #Students类的实例只能有name和age两个属性了
```
但是对Students的子类，父类的__slots__不起作用，除非子类中也定义__slots__，这样子类允许定义的属性就包括了自身的__slots__和父类的__slots__。
#### @property 
相当于为类中的属性变量赋值重构了一个=运算符。
```
class Students(object):
  def get_score(self):
    return self._score

  def set_score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    self._score = value


#实例化Students类，调用get_score 和 set_score设置分数
s = Students()
s.set_score(60)
s.get_score()

#但是每次调用方法麻烦，想直接用=赋值，用s.score得到值，就要用到@property
class Students(object):
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    self._score = value
#这样就可以直接用=了
s = Students()
s.score = 60
print(s.score)

#也可以不写@score.setter，这样s.score就成了只读属性了
```
#### 多重继承
不同于java一类的静态语言，python可以实现多重继承。

所谓多重继承就是子类可以继承多个父类。
***MixIn***就是设计一个类，继承一个主线，其他多继承的父类可以添加其他功能，以MixIn结尾。比如：
```
class MyTCPServer(TCPServer, ThreadingMixIn):
  pass                                                      #编写TCP服务，但加入了多线程模式
```
#### 定制类
***\_\_len__()***

\_\_len__()方法能让len()函数调用这个class，\_\_len__()方法里面要返回class的长度。

***\_\_str__()***

使用该方法，可以让print（class）时打印出__str__()内返回的内容。
```
class Students():
  def __init__(self, name):
    self.name = name
print(Students('Mark'))
#只会返回一个类似<__main__.Student object at 0x109afb190>的结果

#使用__str__后
class Students():
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return 'Students object (name: %s)' %(self.name)
print(Students('Mark'))
#返回Students object (name: Mark)
```
***\_\_iter__()***

在类中加入\_\_iter__()方法，可以使用for循环迭代类，它返回一个可迭代对象。for循环会根据该对象的\_\_next__()方法循环到下一个值，直到遇到Stopteration错误。
```
#实现Fib类
class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1
  def __iter__(self):
    return self
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 10000000:
      raise StopIteration()
    return self.a

for n in Fib():
  print(n)
```
***\_\_getitem__***

在类中使用\_\_getitem__方法，可以将实现类似list或dict一样的下标读取内容的功能。
```
#上面的Fib()没有f[5]取第5个元素的功能，下面用__getitem__实现
class Fib(object):
  def __getitem__(self, n):
    if isinstance(n, int):                    #n是索引
      a, b = 1, 1
      for x in range(n):
        a, b = b, a + b
      return a
    if isinstance(n, slice):                  #n是切片
      start = n.start
      stop = n.stop
      if start is None:
        start = 0
      a, b = 1, 1
      L = []
      for x in range(stop):
        if x >= start:
          L.append(a)
        a, b = b, a + b
      return L
```
***\_\_getattr__***

\_\_getattr__方法可以定制类中没有的属性一旦被访问时的应对方法。
```
#比如Students类中只定义了name属性，而没有score属性，一旦score属性被访问，就会报错
class Students(object):
  def __init__(self, name):
    self.name = name

s = Students('Mark')
print(s.name)
print(s.score)                              #会报错

#这时可以用__getattr__方法定制
class Students(object):
  def __init__(self, name):
    self.name = name
  def __getattr__(self, attr):
    if attr == 'score':
      return 60
#只有当score属性不存在时，才会通过__getattr__查找返回
#一旦使用了__getattr__，没有的属性都会在其中查找，如果__getattr__中也没有，则不会报错，而是返回None
#如果想报错，则需在__getattr__中加上错误信息
class Students(object):
  def __init__(self, name):
    self.name = name
  def __getattr__(self, attr):
    if attr == 'score':
      return 60
    raise AttributeError('\'Students\' object has no attribute \'%s\'' %attr)

#__getattr__也可以返回函数
```
常见用法见[getattr.py](./getattr.py)

***\_\_call__***

\_\_call__可将实例名直接当成函数方法调用。
```
class Students(object):
  def __init__(self, name):
    self.__name = name
  def __call__(self, score = 60):
    print('My name is %s, score is %d.' %(self.__name, score))

s = Students('Mark')
s(90)
```
