#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
'''
Socket:
    Socket 通常称作"套接字",用于描述IP地址和端口,是一个通信链的句柄。

'''
ip_port = ('127.0.0.1',8811)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("等待中.....")
    #等待客户端访问,如果有访问则拿到访问的IP地址的发送来的数据
    conn,addr = sk.accept()
    #有客户访问之后就可以创建一个线程进行访问
    #读取数据,在linux 里需要判断接受到的数据是否有数据,需要判断client_date
    client_data = conn.recv(1024)  #1024 是字符  官方的推荐是不大于8k8192
    #判断如果没读取到数据则退出当前循环等待下次访问
    if not client_data.decode():
        break;
    #输出读取到的内容
    print("访问的IP地址:{0} 说的内容是{1}".format(addr,str(client_data,'utf8')))
    #返回数据
    conn.sendall(bytes('不要回答！不要回答！不要回答！','utf8'))
    #关闭访问
    conn.close()

    '''
        Socket属性:


    '''