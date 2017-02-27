#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
多态
2017年2月27日20:08:10
hd
'''

class Animal(object):
    hobie = 'meat'
    def __init__(self,name):
        self.name = name
    def tale(self):
        print("Subclass must implement.....")

class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__(name)

    def tale(self):
        print("My Is Cat")

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)

    def tale(self):
        print("My Is Dof")

#传入方法执行多态
def Tale(obj):
    obj.tale()

c = Cat('Cat')
d = Dog('dog')

Tale(c)
Tale(d)

