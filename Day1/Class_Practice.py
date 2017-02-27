#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Person(object):
    def __init__(self,name,age,gender):
        self.name =name
        self.age = age
        self.gender = gender

    def SayHello(self):
        print("Name Is %s Age Is %d Gender Is %s"%(self.name,self.age,self.gender))


def main():

    p1 = Person('HD',29,'man')
    p1.SayHello()


if __name__ == '__main__':
    main()