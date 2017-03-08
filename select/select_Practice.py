#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
 Python的select()方法直接调用操作系统的IO接口,它监控sockets,open,files和pipes方法的文件句柄何时变成readata和writeable或者通信错误,
 select() 使得同时监控多个连接变得简单,并且比写一个长循环来等待和监控多客户端连接要高效，因为select直接通过操作系统提供的C的网络接口进行操作,而不是通过Python的解析器。
 select() 方法接受并监控三个通信列表,第一个是所有的输入的data,第二个是输出的data,第三个是错误的data
'''
#例：
import socket,select

def Server():
    addrePoint=('0.0.0.0',8000)
    server = socket()
    server.bind(addrePoint)
    server.listen(1000)

    inputs =[server]
    outputs = []

'''
    所有客户端的进来的链接和数据将会被server的主循环程序放在上面的list中处理。
'''





