#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
数字:
    在Python中,数字并不是一个真正的对象类型,而是一组类似类型的分类。
    Python数字类型的完整工具包括:
        整数和浮点数
        复数
        固定精度的十进制数
        有理分数
        集合
        布尔类型
        无穷的整数精度
        各种数字内置函数和模块

    使用math 模块必须导入math数学模块

生成随机数:
    如果生成想生成随机数,那么就需要导入random 模块来生成随机数
'''

import math #数字模块
import random

print(math.sqrt(144))
print(pow(144,4,3))  #这个类似于 144 ** 4  第三个参数就是   144**4%3 得出一个结果

obj = random.random() #生成随机小数
print(obj)
objInt = random.randrange(100) # 生成比参数里数字小的随机数
print(objInt)
objI = random.randint(1,200) #生成参数1和参数2之间的随机数
print(objI)

objS = random.choices(["HouDong","NaNa","KK",'JJ'],k=2) #根据参数1里的列表随机生成一个列表, k 是代表生成的个数 默认是一个
print(objS)
objS1 = random.choice(["HouDong","NaNa","KK",'JJ']) #根据参数里的列表随机生成一个参数返回
print(objS1)