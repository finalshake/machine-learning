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

