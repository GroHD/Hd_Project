#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
2017-02-28 11:23:20
HD
FOR练习学习
'''
#循环输出大写字母
for c in 'spam':
    print(c.upper())
#输出一个数的平方 range() 拿到一个从0到6的列表,在2.0里输出的是一个[1,2,3,4,5,6] 但是在3.0里输出的是[0:6]，这样可以节省内存空间
for x in range(6):
    print(x**2)

