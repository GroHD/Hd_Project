#!/usr/bin/env python
#-*- coding:utf-8 -*-

#定义一个类,继承object
class Person(object):
    #类变量
    num_count =0
    #初始化方法
    def __init__(self,name,age,gender):
        self.name =name
        self.age = age
        self.gender = gender
    #普通方法
    def SayHello(self):
        print("Name Is %s Age Is %d Gender Is %s"%(self.name,self.age,self.gender))
#一个学生类继承Person
class Student(Person):
    def __init__(self,name,age,gender,fenshu):
        #实现父类的初始化方法
        super(Student,self).__init__(name,age,gender)
        self.fenshu = fenshu
    def Print(self):
        print("SayHell %s"%(self.name))

def main():

    p1 = Student('HD',29,'man',22)
    p1.Print()


if __name__ == '__main__':
    main()