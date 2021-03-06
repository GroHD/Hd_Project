#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
动态变量, 即使你没有告诉python 编译器 某个变量的变量类型是什么，Python也可以根据 赋值的值类型进行判断该变量类型是什么

创建变量:
        一个变量,当代码第一次给他赋值的时候就创建了它。之后的赋值将会改变已创建的变量名的值。
变量类型:
        变量永远不会有任何的和它相关的类型信息或约束。类型的概念是存在于对象中而不是变量中。

    变量在赋值的时候才创建,它可以引用任何类型的对象，并且必须在引用之前赋值。

'''

#例:

a = 3
print(a)
'''
    上面的例子Python 会执行三个不同的步骤去完成这个请求：
        1.创建一个对象来代表值3
        2.创建一个变量a,如果它还没有创建的话
        3.将变量与新的对象3相连接
    变量和对象是保存在内存中的不同部分,并通过链接相关联
    类型是属于对象的,不是属于变量

    变量是一个系统表的元素,拥有指向对象的连接的空间。
    对象是分配一快内存，有足够的空间去表示他们所代表的值
    引用是自动形成的从变量的对象的指针
'''
