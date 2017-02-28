#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
2017-02-28 11:23:20
HD
字典练习学习
'''

rec ={"name":{"first":'HD',"last":"dd"},'job':['dev','msgr'],'age':40.5}
print(rec['name'])#找到name keys 下的value
print(rec['name']['first']) #找到name 下的first keys
print(rec['job']) #找到job 列表
print(rec['job'][-1]) #拿到job 列表里最后一个值
rec['job'].append('janitor') #向job 表里添加数据
print(rec)
#rec = 0 #清理内存对象

print("Keys:",rec.keys()) #拿到字典的keys
print("VALUES:",rec.values()) #拿到字典的Values

#循环输出keys和对应的vlue
for key in rec.keys():
    print(key,"=>",rec[key])

#可以使用sorted 来给字典进行排序
for k,v in sorted(rec):
    print(k,"=>".v)