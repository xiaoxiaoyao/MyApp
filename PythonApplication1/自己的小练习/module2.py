#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self,name):
        self.__name = name # 双下划线，表示private，机制上阻止访问，调用p.__name错误
    @property
    def age(self):
        return self._age  # 单下划线，表示protected，原则上不允许访问，但调用p._name可以访问到
    @age.setter
    def age(self,value):
        if type(value) != int:
            raise ValueError('need a interger')
        if not (0< value <150):
            raise ValueError('need a reasonable number')
        self._age = value
         # 以上写成self.age = value会报错，因为当设置了getter/setter后，
         # 对属性的直接访问会调用该属性对应的getter/setter
         # 这里写成self.age相当于又调用了一次age的getter方法，最终会导致递归调用栈溢出

p = Person('xx')
p.age = 10 ; # 当设置了getter/setter后，对属性的直接访问会调用该属性对应的getter/setter
print(hasattr(p,'age'))
print(hasattr(p,'_age')) # true
print(hasattr(p,'__name')) # false

# python对象权限机制并不阻止访问,一切皆靠自觉
try:
    print(p.__name) # error 没有该属性
    print(p.name) #error 没有该属性
except ValueError as e:
    print(e)
finally:    
    print(p._Person__name) # 强行访问私有变量
    print(p._age)  # 受保护属性，不建议直接访问，应该使用getter，setter访问
    print(p.age) #ok