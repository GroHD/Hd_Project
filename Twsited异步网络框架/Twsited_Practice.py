#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD

   Twsited是一个时间驱动的网络框架，其中包含了诸多功能m例如：网络协议，线程，数据库管理，网络操作，电子邮件等
'''

r'''
    Protocols
        Protocols 描述了如何以异步的方式处理网络中的事件,http,SND以及IMAP是应用层协议中的例子
        Protocols 实现了IProtoco接口,它包含如下的方法:
            makeConnection   在transport对象和服务器之间建立一条连接
            connectionMade  连接建立起来之后调用
            dataReceived    接受数据时调用
            connectionLost  关闭连接时调用
    Transport
        Transport 代表网络中两个通信节点之间的连接，比如连接里描述的细节，连接时面向流失的还是面向数据报的，流控记忆可靠性。
        Transport 实现了ITransports 接口,它包含如下方法:
            write   以非阻塞的方式按顺序依次将数据写到物理连接上,发送数据的时候必须发送byes字节
            writeSequence   将一个字符串列表写到物理连接上
            loseConnection  将所有挂起的数据写入,然后关闭连接
            getpeer 获取连接中对端的地址信息
            getHost 获取链接中本端的地址信息

            将transports 从协议中分离出来也使得对这两个层次的测试变得更佳简单。


'''

from twisted.internet import protocol,reactor   #reactor 类似于select 一样


class Echo(protocol.Protocol):
    def dataReceived(self, data): #接受到数据之后调用这个方法
        self.transport.write(data) #把收到的数据返回给客户端

def main():

    factory = protocol.ServerFactory() #定义一个基础的工厂类
    factory.protocol = Echo

    reactor.listenTCP(8800,factory) #检测 8800端口
    reactor.run()



if __name__ == '__main__':
    main()