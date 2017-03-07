#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
'''
双向队列(deque)
    //创建队列
    import collections
    dq = collections.deque()
    队列里的方法:
    append(Object) #向队列中添加数据
    appendleft(Object)#向队列左侧添加数据
    clear() #清空队列
    count(Obj) #查看队列中的某个元素出现了多少次
    extend(ListObj) #扩展是向右边扩展
    extendleft(ListObj) #向左边扩展
    例：
    dq = collection.deque()
    dq.append('1') #添加
    qd.appendleft('2') #向左添加
    qd.extend(['a','b','c']) #向右扩展
    qd.extendleft(['l','k','o']) #向左侧扩展
    结果:
    print(dq)
    ['l','k','o','2','1','a','b','c']
     index(Obj,Star,End)  #取出某个值得位置,第二个和第三个参数可以为空,第二个是从哪个位置开始查询该值,第三个参数就是查询到那个位置结束,默认从左测开始查询
    insert(Obj,index) # 插入数据
    pop(Obj) #q取出数据,并且移除数据,从右侧开始
    popleft(Obj) #取出数据,并且移除该数据,从左侧开始
    rotate(index)# 可以把一些队列中的数据排到队列的前边
'''
'''
    单项队列在 线程中有详细介绍
'''