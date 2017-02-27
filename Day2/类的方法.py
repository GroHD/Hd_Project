#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name
    hobbie = 'meta'
    @classmethod  #类的方法
    def talk(self):
        print("%s is talking..."%(self.hobbie)) #错误不可以访问实例变量,只可以访问类变量,self.hobbie 是可以访问的
    @staticmethod
    def walk():
        print("这个不需要self,对象可以直接访问")
    @staticmethod
    def walkTwo(self):
        print("这个方法访问必须传入对象自己")
    @property
    def habit(self):
        print("这个方法是对象的属性")

    #下面是给方法设置赋值和取值属性
    @property
    def play_total(self):
        return self.num

    @play_total.setter
    def play_total(self,num):
        self.num = num
    @play_total.deleter  #加一个删除属性
    def play_total(self):
        del self.num
a = Animal('HouDong')

a.walkTwo(a) #传入自己的方法
a.habit #方法加特性之后成为属性
a.walk() #调用没有参数的sttaic methon
a.talk() #不可以访问实例变量
a.play_total = 12
del a.play_total #删除某个变量
n = a.play_total
print("Seting Play_tital %d"%(n))