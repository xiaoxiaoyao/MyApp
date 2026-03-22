#!/usr/bin/env python
# -*- coding: utf-8 -*-
print '''hello
world,
my name is
huoshan'''
print '============================'
print '\\\\'
print r'\\\\\n\r'# r->raw
print '============================'
print ord('A')#65
print chr(70)#F
print u'中文'
print '============================'
print '亲爱的%s你好！你%d月的话费是%.2f，余额是%.2f' % ('huoshan', 12, 58.5, 12.5)
print 'growth rate: %d %%' % 7
print '===================list===================='
# list是一个可变的有序表
classmates = ['huoshan', 'bingqilin', 'zhangsan']
print classmates
print classmates[1]
print 'classmates lens ==', len(classmates)
print classmates[-1]
classmates.append('lisi')#['huoshan', 'bingqilin', 'zhangsan', 'lisi']
print classmates
classmates.insert(1, 'jack')#['huoshan', 'jack', bingqilin', 'zhangsan', 'lisi']
print classmates
classmates.pop()#['huoshan', 'jack', bingqilin', 'zhangsan']
print classmates
classmates.pop(2)#['huoshan', 'jack', 'zhangsan']
print classmates
classmates[2] = 'rose'#['huoshan', 'jack', 'rose']
print classmates
person = ['178cm', 18, 90.5, True]#list里面的元素的数据类型也可以不同
print person
language = ['java', ['c', 'c++'], 'php', 'python']#list元素也可以是另一个list
print language
print language[1]#['c', 'c++']
print language[1][1]#c++
empty_list = []
print len(empty_list)#0
print '===================tuple===================='
# tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('huoshan', 'bingqilin', 'zhangsan')
print classmates[0]
# classmates[0] = 'huoshan' TypeError: 'tuple' object does not support item assignment
empty_tuple = ()
print len(empty_tuple)
one_tuple = (1)#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
			   #这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
print one_tuple
one_tuple = (1,)#有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print one_tuple
change_tuple = ('a', ['A', 'B'], 'c')
print change_tuple[1][1]
change_tuple[1][1] = 'X'#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
						#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，
						#tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，
						#就不能改成指向其他对象，但指向的这个list本身是可变的！
						#要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
print change_tuple#('a', ['A', 'X'], 'c')
print '===================if and while===================='
age = 20
if age >= 18:#注意不要少写了冒号:
	print 'adult'
elif age >= 6:
	print 'teenager'
else:
	print 'too young too simple'

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if None:
	print True#won't print
if 0:
	print True#won't print
if 1:
	print '1', True
if '':
	print True#won't print
if []:
	print True#won't print

# for in
# classmates = ('huoshan', 'bingqilin', 'zhangsan')
for name in classmates:
	print name

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + i
print sum

# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
# 可以生成一个整数序列，比如range(5)生成的序列是从0开始小于5的整数：
sum = 0
for i in range(11):
	sum = sum + i
print sum

# range(101)就可以生成0-100的整数序列，计算如下：
# 结果是当年高斯同学心算出的5050
sum = 0
for i in range(101):
	sum = sum + i
print sum

'''
age = raw_input('please input your age:')
if int(age) > 18:#we need transform
	print 'your age is bigger than 18'
'''
print '==========================dict==========================='
# dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，
# 如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过
# key计算位置的算法称为哈希算法（Hash）。
person = {'name': 'huoshan', 'age': 28, 'score': 95.5}
print person
print person['age']
person['score'] = 88
print person
if 'name' in person:#if key is in dict
	print 'yes'
print person.get('name'), person.get('height'), person.get('height', -1)
person.pop('score')
print person
print '==========================set==========================='
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([5, 1, 2, 3, 2, 1, 3, 4])# 重复元素在set中自动被过滤
print s
s.add(4)
print s
s.remove(5)
print s
if 6 in s:
	s.remove(6)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print 's1 & s2 :', s1 & s2
print 's1 | s2 :', s1 | s2
# set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
'''
s.add([1, 2])#TypeError: unhashable type: 'list'
'''
# 不可变对象(str是不变对象，而list是可变对象)
a = ['b', 'a', 'c']
a.sort()
print a
a = 'abc'
print a.replace('a', 'A')#replace方法创建了一个新字符串'Abc'并返回
print a
print '==========================function==========================='
# 内置函数;doc:https://docs.python.org/2/library/functions.html
print abs(-20)
print cmp(1, 2), cmp(1, 1), cmp(2, 1)
print int('12'), int(12.34), float('12.34'), str(1.2), bool(1), bool(''), unicode(100)
my_abs = abs#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
print my_abs(-100)

PI = 3.14
def area_cycle(r):
	return PI * r * r
print area_cycle(3)

# 定义一个什么事也不做的空函数,如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
	pass

# 参数类型做检查
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('it is type error')
	if x > 0:
		return x
	else:
		return -x
print my_abs(-10)

# 返回多个值
def point(x, y):
	return x, y
m, n = point(3, 4)
print m, n
print point(3, 4)#但其实这只是一种假象，Python函数返回的仍然是单一值
				 #原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
				 #而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python
				 #的函数返回多值其实就是返回一个tuple，但写起来更方便。
m, n = (5, 6)
print m, n

# 默认参数
#几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print power(2, 3)#8
print power(2)#4

def show_student(name, gender, age=10, city='Beijing'):
	print 'name:', name
	print 'gender:', gender
	print 'age:', age
	print 'city:', city

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
print '********************************************'
show_student('huoshan', 'M', 28, 'Nanjing')
print '********************************************'
show_student('huoshan', 'M', 18)
print '********************************************'
show_student('huoshan', 'F', city='Nanjing')
print '********************************************'

# 可变参数,可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def add(*values):
	sum = 0
	for v in values:
		sum = sum + v
	return sum

print add()
print add(1, 2)
print add(1, 2, 3)
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
l = [1, 2, 3, 4]
print add(*l)#这种写法相当有用，而且很常见。

# 关键字参数,关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，
# 我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
# 我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
def person(name, age, **kw):
	print 'name:', name, ' | age:', age, ' | other:', kw

person('huoshan', 28)
person('huoshan', 28, city='Nanjing')
person('huoshan', 28, city='Nanjing', love='python', gender='M')
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
d = {'city': 'Beijing', 'height': '180cm'}
person('huoshan', 28, **d)

# 参数组合,在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
# 这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数和关键字参数。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''---------------TODO参数组合还不是太了解，有点绕人 -----------------'''
# 高级特性
# 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
print '=============================高级特性:切片==============================='
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
print L[0:3]#表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print L[:3]#如果第一个索引是0，还可以省略
print L[1:3]#也可以从索引1开始，取出2个元素出来
print L[-2:]

L = range(100)#0-99
print L
print L[:10]#0-9
print L[-10:]#90-99
print L[10:20]#10-19;前11-20个数
print L[:10:2]#[0,2,4,6,8];前10个数，每两个取一个
print 'all:', L[:]#所有数
print L[::5]#所有数，每5个取一个
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print (1, 2, 3, 4, 5, 6)[0:4]
# 字符串也可以用切片操作
# 在很多编程语言中，针对字符串提供了很多各种截取函数，其实目的就是对字符串切片。
# Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
# 有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。
print 'hello world'[0:7]
print 'hello world'[::2]
print '=============================高级特性:迭代==============================='
# Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key

for value in d.itervalues():
	print value

for k, v in d.iteritems():
	print k, v
# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 判断一个对象是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(123, Iterable)
print isinstance([1, 2, 3], Iterable)
# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate
# 函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
	print i, value

# for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码
for x, y in [(0, 0), (1, 3), (4, 9), (5, 5)]:
	print x, y
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
print '=============================高级特性:列表生成式==============================='
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print range(1, 11)
print [x * x for x in range(1, 11)]#写列表生成式时，把要生成的元素x * x放到前面，
								   #后面跟for循环，就可以把list创建出来，十分有用，
								   #多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print [x * x for x in range(1, 11) if x % 2 == 0]
# 还可以使用两层循环，可以生成全排列：
p = 'a'
q = 'b'
print [p + q]#contact
print [m + n for m in 'ABC' for n in 'XYZ']
# 列出当前目录下的所有文件和目录名
import os
print [d for d in os.listdir('/home')]
# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]
# 把一个list中所有的字符串变成小写
l = ['JAVA', 'PHP', 'PYTHON', 'C++', 12]
print [s.lower() for s in l if isinstance(s, str)]
print '=============================高级特性:生成器==============================='
# TODO not OK
print '=============================高阶函数==============================='
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):#编写高阶函数，就是让函数的参数能够接收别的函数。
	return f(x) + f(y)
print add(-3, 5, abs)
print '=============================高阶函数:map/reduce==============================='
# Python内建了map()和reduce()函数。
def f(x):
	return x * 2
print map(f, [1, 2, 3, 4])

def lower(x):
	return x.lower()
print map(lower, ['JAVA', 'PHP', 'PYTHON', 'C++'])
# reduce
def f2(x, y):#这个函数必须接收两个参数,reduce把结果继续和序列的下一个元素做累积计算
	return x * y
print reduce(f2, [1, 2, 3, 4])#1*2+3*4=24
# reduce TODO not OK
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def standard_name(name):
	l = name.lower()
	return l.replace(l[0], l[0].upper())
print map(standard_name, ['huoshan', 'ZHANGSan', 'lisI'])
print '=============================高阶函数:filter==============================='
# Python内建的filter()函数用于过滤序列。
# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
	return n % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])
# get string which contains 's'
def has_s(s):
	return 's' in s
print filter(has_s, ['nice', 'miss', 'Spring'])
print '=============================高阶函数:sorted==============================='
print sorted([1, 3, 2, 4, 9, 5, 1])
# sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
# 比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([1, 3, 2, 4, 9, 5, 1], reversed_cmp)
print sorted(['bob', 'about', 'Zoo', 'Credit'])#默认情况下，对字符串排序，是按照ASCII的大小比较的，
											   #由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
											   #['Credit', 'Zoo', 'about', 'bob']
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)#忽略大小写的排序
print '=============================返回函数=============================='
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print lazy_sum(1, 3, 5, 7, 9)
print f
print f()
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2#False,f1()和f2()的调用结果互不影响。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
print f1()#9
print f2()#9
print f3()#9
print '=============================匿名函数=============================='
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，
也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f = lambda x: x * x
print f
print f(4)
# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
print build(1, 2)()
print '=============================装饰器=============================='
def now():
	return '2015-12-07'
f = now
print f()
print now.__name__
print f.__name__
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	return '2015-12-07'
print now()#TODO not OK
print '=============================偏函数=============================='
print int('12345')#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print int('12', base=8)#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)
print int2('1000000')
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3 = functools.partial(int, base=2)
print int3('1000001')
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print int3('1000000', base=10)#也可以在函数调用时传入其他值
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

