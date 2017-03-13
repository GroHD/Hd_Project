#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
    Type 对象类型:
        对内置函数type(x)  能够返回对象x的类型对象，类型对象可以用在Python中的if语句来进行手动类型比较。
        调用这些名称事实上是对这些对象构造函数的调用,而不仅仅是转换函数,不过作为基本的使用来说，还是可以把他们当作简单的函数的。
        在python 中也可以使用isinstance函数进行类型测试。
    例：
        type([1]) == type([])
        type([1]) == list
        isinstance([1],list)
        上面所有类型测试都是真

        import types
        def f():pass

        type(f) == types.FunctionType
        上面的也是真

        目前python 的类型也可以再分为子类，一般都建议使用isinstance技术

'''