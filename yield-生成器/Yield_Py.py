#!/usr/bin/env python
#-*- coding:utf-8 -*-



def foo(x):
    print('Next Start')
    yield x**3 #运行到这里就会跳出该方法，next的时候就会从该处继续向下执行
    print('Next End')

def main():
    f = foo(10)
    print(next(f))#到yield 的时候就会跳出该函数然后返回yield后面的值
    next(f) #继续从该函数的yield的地方继续向下执行，直到遇到下一个yield或执行完函数

if __name__ == '__main__':
    main()