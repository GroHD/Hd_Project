#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
import socket
ip_point=('127.0.0.1',8813) #连接到socket多线程
#创建实例对象
sk = socket.socket()
#设置访问的服务器ip地址
sk.connect(ip_point)
#发送数据
sk.sendall(bytes('呼叫!不叫!','utf8'))
#接受服务器返回的数据
client_data = sk.recv(1024)

#打印出服务器返回的数据
print(str(client_data,'utf8'))
print("发送成功！！！")
#关闭客户端
sk.close()