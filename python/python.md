### 高级特性
#### 切片
list或tuple中可以使用':'
```python
  l[3:6]          #that is l[3] l[4] l[5]
  l[:6]           #that is l[0] to l[5]
  l[-1]           #the last one
  l[-2]           #the one before last one
  l[1:6:2]        #l[1] to l[5] 每两个取一，即l[1] l[3] l[5]
```
#### 迭代
python 的for循环可以使用 for in 作用于list,tuple,dict
```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for k in d:
...     print(k)
...
a
c
b
```
```python
>>>for v in d.values():
...     pass
```
```python
>>>for k, v in d.items():
...     pass
```
#### 列表生成式
生成list ［1-10] 可使用：
```python
list(range(1,11))     #不包括11
```
```python
[x * x for x in range(1, 11)]   #生成[1*1, 2*2, ... , 10*10]
[m + n for m in 'ABC' for n in 'XYZ']   #列出['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```
#### 生成器
python在生成list或tuple时，如果包含元素很多，可以不用一次全部生成，而是迭代到哪生成到哪。
有两种生产方法：
1. 直接在列表生成式中，将［］改为（）
```python
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
```python
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
```python
from collections import Iterable
isinstance([],m Iterable)             #返回True
```
判断对象是否是迭代器Iterator：
```python
from collections import Iterator
isinstance(g, Iterator)               #返回True
```
Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

Python的for循环本质上就是通过不断调用next()函数实现的：
```python
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
```python
f = abs(-10)              #f是10
f = abs                   #f是abs函数，可以用f(-10)
abs = 10                  #此时调用abs(-10)会报错，因为abs已经被改为值是10的变量
```

map()函数：接受两个参数，一个是函数，一个是Iterable（例如list）

map将函数依次作用在Iterable的每个元素上，把结果以Iterator形式返回。
```python
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))     #将list中的数字转换为字符串，返回['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

reduce()函数：接受一个函数和一个序列，但接受的函数必须有两个参数
```python
from functools import reduce
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```
***filter***

filter()函数即过滤筛选函数，接受一个函数和一个序列，函数的返回值是True或False，根据返回值的真假依次决定序列元素的去留。
```python
#删除序列中的空字符
def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['a', '', 'b', ' ', None]))
#返回['a', 'b']
```
***sorted***

sorted()函数,即排序函数，接受一个序列，也可一带一个函数来表明排序条件。
```python
sorted([36, 5, -12, 9, -21])                        #返回[-21, -12, 5, 9, 36]
sorted([36, 5, -12, 9, -21], key = abs)             #返回[5, 9, -12, -21, 36]
sorted([36, 5, -12, 9, -21], reverse=True)          
#key接受的函数先作用于前面的list或dict等，形成新的序列，然后再用sorted排序
```
#### 返回函数
返回函数即将一个函数名作为函数的返回值。
```python
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
```python
def add(x, y):
  return x + y
#等价于
lambda x, y: x + y
```

#### 装饰器decorator
装饰器是一种特殊的返回函数。一般情况下，如果想在其他函数执行时记录时间或者log，又不想重新在原来函数内部增加东西破坏结构，
就需要用到装饰器。
```python
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
```python
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
```python
class Students(object):
  __slots__ = ('name', 'age')                           #Students类的实例只能有name和age两个属性了
```
但是对Students的子类，父类的__slots__不起作用，除非子类中也定义__slots__，这样子类允许定义的属性就包括了自身的__slots__和父类的__slots__。
#### @property 
相当于为类中的属性变量赋值重构了一个=运算符。
```python
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
```python
class MyTCPServer(TCPServer, ThreadingMixIn):
  pass                                                      #编写TCP服务，但加入了多线程模式
```
#### 定制类
***\_\_len__()***

\_\_len__()方法能让len()函数调用这个class，\_\_len__()方法里面要返回class的长度。

***\_\_str__()***

使用该方法，可以让print（class）时打印出__str__()内返回的内容。
```python
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
```python
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
```python
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
```python
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
```python
class Students(object):
  def __init__(self, name):
    self.__name = name
  def __call__(self, score = 60):
    print('My name is %s, score is %d.' %(self.__name, score))

s = Students('Mark')
s(90)
```
### IO编程
#### 文件读写
```python
with open('path_to/file', 'rwab') as f:                   #r——读，w——写，a——追加写入不覆盖，b——二进制格式
  f.read(size)                                            #一次性读取size大小的内容
  f.readline()                                            #读取一行
  f.readlines()                                           #一次性读取全部，按行返回list
  f.write()
```
#### StringIO & BytesIO
file-like-object, 数据可以写在文件中，也可以写在内存里。

StringIO是在内存中读写str的，BytesIO是在内存中读写二进制数据的。
```python
from io import StringIO
f1 = StringIO()
f2 = StringIO('Hello!\nHi!\nBye!')
f1.write('hello')
print(f1.getvalue())                                      #getvalue()可以一直使用，而read之类函数使用后会指向末尾
f2.readline()

from io import BytesIO
b = BytesIO(b'\xe4\xb8')
b.read()
b2 = BytesIO()
b2.write('yes')
print(b2.getvalue())
```
#### 序列化
将内容、数据（list、dict等）序列化，以便于在网络或串口通信中传输。
* python内置的pickle包
```python
import pickle
pickle.dumps(list)                                        #直接将数据转换为bytes
pickle.dump(dict, file)                                   #直接将数据转换为bytes并写入文件file
pickle.loads(obj)                                         #将obj中bytes反序列化出对象
pickle.load(f)                                            #直接从文件f中反序列化出对象
```
* JSON
```python
import json
json.dumps(dict)                                          #将对象dict内容转变为json格式，返回json格式字符串
json.dump(list, file)                                     #直接将对象list内容序列化为json写入file文件
json.loads(str)                                           #从str字符串中反序列化出对象内容
json.load(file)                                           #从file文件中反序列化对象
```
### 进程和线程
#### 多进程
* 使用multiprocessing模块中的Process类创建一个新的子进程。
* 使用multiprocessing模块中的Queue或者Pipe实现进程之间的通信。
* 使用multiprocessing模块中的Pool创建进程池，批量创建子进程。
* 使用subprocess模块从外部启动程序创建子进程。
***Note***: Process.join()方法等待子进程结束后再继续往下运行。

***Note***: Pool.join()方法必须先调用close()方法，调用close()之后就不能再向Pool中添加新进程了，join()方法等待所有子进程执行完毕。

使用multiprocessing模块使用示例见[multiprocess.py](./multiprocess.py)以及[multiprocess_pool.py](./multiprocess_pool.py)。

subprocess模块：
```python
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
```
```python
# 相当于执行命令nslookup后手动输入
#set q=mx
#python.org
#exit
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```
#### 多线程
* 使用threading模块，用法十分类似multiprocessing模块，threading.Thread()方法创建新的线程，th.start()方法开始线程，th.join()方法
等待线程结束后再往下运行。

* 使用threading.Lock()方法创建锁，锁可以确保同时只有一个线程在运行，防止了全局变量被多个线程交替执行时改乱。

详细示例见[thread.py](./thread.py)。

#### ThreadLocal
ThreadLocal本身是全局变量，可以看成是全局dict，而ThreadLocal.xxx属性都是线程的局部变量。它给每个线程绑定了其特有的局部变量，这样线程执行时
就带着这些绑定的变量运行，防止其他变量被修改，也省去了不断传入参数的麻烦。

通常用法是给线程绑定HTTP请求，数据库链接，用户身份信息等，这样线程调用到的函数就方便访问这些资源了。

更改了上一个thread.py示例，加入ThreadLocal，实现每个线程有每个线程的counter，以及各自的开始结束口令。详见[threadlocal.py](./threadlocal.py)。 
#### 分布式进程
***Note***: multiprocessing模块中的queue类和python直接内置的Queue.queue()是有区别的，multiprocessing中的queue是专门为进程间通信设计的
队列，可以在进程间共享数据；而内置的queue只是单纯的队列，不能在进程间共享。

分布式进程是主进程通过网络给多个机器分发任务，并接收返回的处理结果。队列Queue中存放着要分发的任务，另一个Queue中存放返回的出来结果。
通过multiprocessing模块的managers模块来处理Queue。
```python
# 分发任务的主进程
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
```
```python
# 处理任务的程序，可以在其他机器上，也可以在本机
# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
```
### 正则表达式
* \d          数字
* \w          字母或数字
* .           任意字符
* \s          空格（包括Tab）
python 使用re模块来处理正则表达式。
```python
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
#匹配成功则返回Match对象，否则返回None
#使用r就可以放心得键入正则表达式，不需再考虑python自身的转义字符了

re.split(r'[\s\,]+', 'a,b, c   d')
#split是切割方法

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.group(0)                                            #group(0)代表整个字符串
m.group(1)                                            #group(1)开始代表后续分组的字符串
m.groups()                                            #返回所有分组组成的tuple

#对于要重复使用的正则表达式，可以预先编译以节省运行时间
x = re.compile(r'^(\d{3})-(\d{3,8})$')
x.match('010-12345').groups()
```

### 异步IO
CPU计算速度一般快于IO读写速度，同步IO一旦遇到IO时便阻塞，等待IO读写结束才继续执行下面的程序；也可以使用多线程或多进程
来解决IO阻塞的问题，但大规模使用多线程或多线程，时间会浪费在线程\进程的切换上，效率也不高。异步IO解决了在一个线程中IO
阻塞的问题，遇到IO读写后直接执行下面的程序，直到IO读写完成返回结果再处理IO结果。
#### 预备知识
* 生成器generator的方法next()和send()
```python
#next()对生成器单步迭代
#send()与next()差不多，差别在于：send()必须带参数
#send()的参数是None时，等价于next()
#send()的参数不为None时，将参数直接传给了generator中yield的返回结果值,send方法会首先把上一次挂起的yield语句的返回值通过参数设定
#在一个生成器对象没有执行next方法之前，由于没有yield语句被挂起，所以执行send方法会报错
def gen():
  value = yield 1
  value = yield value

g = gen()
print(next(g))                      #打印出了1
print(g.send(2))                    #send(2)先将参数2传给了上次挂起的yield 1 的返回值，再执行下一句yield value, 打印2
print(g.send(3))                    #send(3)将参数3传给yield value 的返回值 value，继续运行发现gen（）结束，抛出StopIteration异常

#若直接send（2），会报错
g = gen()
print(g.send(2))                    #TypeError: can't send non-None value to a just-started generator
```
* yield from
yield from 后面必须接一个可迭代对象iterable。
```python
#yield 与 yield from区别
def yield_func(list):
  yield list

def yield_from_func(list):
  yield from list

list = ['a','b','c']
yield_gen = yield_func(list)
for i in yield_gen:
  print(i)                                      #打印出了['a','b','c']

yield_from_gen = yield_from_func(list)
for i in yield_from_gen:
  print(i)                                      #打印出了a, b, c

#yield只是将后面的对象抛出，而yield from将后面iterable对象每一个元素依次抛出
```
#### 协程
协程Coroutine,是一种子程序，其内部可以中断，中断后执行其他子程序，适时再回来继续执行。

python通过生成器generator实现协程，内部用yield中断程序，外部用next()或send来返回继续执行。
```python
def consumer():
  ret = ''
  while True:
    n = yield ret
    if not n:
      return
    print('CONSUMER Consuming %s...' %n)
    ret = '200 OK'

def produce(con):
  con.send(None)
  n = 0
  while n < 5:
    n += 1
    print('PRODUCER Producing %s...' %n)
    r = con.send(n)
    print('PRODUCER Consumer return %s' %r)
  con.close()                                       #最后一定要关掉consumer

con = consumer()
produce(con)
```

***asyncio***是python内置的异步IO模块。
