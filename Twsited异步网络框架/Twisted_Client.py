#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD

   客户端
'''

from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):#连接一建立成功,就会自动调用此方法
        self.transport.write(b'hell Word!')

    def dataReceived(self,data):#当有数据返回时调用该方法
        print("Server said :",data)
        self.transport.loseConnection() #关闭连接

    def connectionLost(self, reason): #关闭连接
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason): #连接不上调用该方法
        print("Connecton failde --goodbye!")
        reactor.stop()
    def clientConnectionLost(self,connector,reason):#在连接的过程中断开了调用该方法
        print("关闭数据")
        reactor.stop()

def main():
    f = EchoFactory()
    reactor.connectTCP('127.0.0.1',8800,f)#连接服务器
    reactor.run() #运行

if __name__ == '__main__':
    main()