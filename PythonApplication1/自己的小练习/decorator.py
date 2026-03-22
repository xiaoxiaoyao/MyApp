# -*- coding: utf-8 -*-
#在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

import time
print(time.asctime())

def log(func):
    def wrapper(*args,**kw):
        print('call 1 %s'%func.__name__)
        return func(*args,**kw)
    print('call 0 %s'%func.__name__)
    return wrapper

newtime=log(time.asctime)
print(newtime())