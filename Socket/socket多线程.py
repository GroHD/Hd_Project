#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD

    SocketServer 多线程
        多线程使用的类:
            class socketserver.ForkingTCPServer
            class socketserver.ForkingUDPServer
            class socketserver.ThreadingTCPServer
            class socketserver.ThreadingUDPServer

        可以使用:
            self.request.XXX() 来拿客户端发送过来的数据

'''

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    #在下面处理客户端访问的数据，这个必须这样
    def handle(self):
        #拿到客户端发送过来的数据
        #self.request 类里有所有socket里的方法，可以直接调用
        data = self.request.recv(1024)
        print("Client Says:",str(data,'utf8')) #处理编码
        self.request.send(bytes("收到！收到！！！",'utf8'))
        client_Address = self.client_address #拿到客户端访问地址
        print("访问地址:",client_Address)
    def setup(self):
        print("进入handle 之前调用")

    def finish(self):
        print("执行完handle 的时候调用")

if __name__ == "__main__":
    HOST,PORT = 'localhost',8813
    #绑定ip地址和端口,和接收到客户端访问之后需要调用那个方法
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    #开始监听调用端口
    server.serve_forever()
