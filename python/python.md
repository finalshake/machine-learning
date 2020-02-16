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
