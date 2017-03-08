#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    协程又称微线程,一句话说明协程就是一种用户态的轻量级线程。
    协程拥有自己的寄存器上下文和栈。
    协程只能保留上一次调用时的状态,每次过程重入时,就相当于进入上一次调用的状态,也就是说进入上一次离开时所处逻辑流的位置
    协程一般都是在单线程里运行的,协程是不可以多线程的
    协程的好处:
        1.无需线程上下文切换的开销。
        2.无须原子操作锁定及同步的开销
        3.方便切换控制流，简化变成模型
        4.高并发+高扩展性+低成本,一个CPU支持上万个协程都不是问题,所以很适合用于高并发处理。

    协程的缺点：
        1.无法利用多核资源，协程的本质是个单线程，它不能同时将单个CPU的多个核用上,协程需要和进程配合才能运行在多CPU上,一般普通日常编写的绝大部分应用都没有这个必要,除非是cpu密集型应用
        2.进程阻塞操作,会阻塞掉整个程序


#例:
#使用yield实现协程操作例
import time
import queue
def consumer(name):
    print("----->starting eating baozi.....")
    while True:
        new_yelid = yield
        print("yield Next...")

if __name__ == '__main__':
    c = consumer('hd')
    c.__next__()
    c.__next__()
'''
r'''
    Gevent
        Gevent是一个第三方库,可以轻松通过gevent实现并发同步或异步编程,在gevent中用到的主要模式是Greenlet,它是以C扩展模块形式介入Python的轻量级协程，Greenlet全部运行在主程序操作系统进程的内部,但他们被协作地调用

import gevent

def foo():
    print("Runing in foo")
    gevent.sleep(0) #进行切换到下一个方法执行
    print("Explicit context switch to foo again")

def bar():
    print("Explicit context to var")
    gevent.sleep(0) #切换到下一个方法执行
    print("Implicit context switch back to bar")

gevent.joinall(
    [
        gevent.spawn(foo),
        gevent.spawn(bar)  #这里可以添加多个方法,这个会依次进行运行
    ]

)
'''
r'''
    通过gevent 实现单线程下的多socket并发
'''
import gevent
from gevent import monkey,socket
monkey.patch_all()# 这个的作用就是把网络库,IO等线程都变成一个非阻塞

def  server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(5000)
    while True:
        cli,addr = s.accept()
        print("IP:%s 访问到服务器了..."%(addr[0]))
        gevent.spawn(handle_request,cli)
#处理请求结果
def handle_request(s):
    try:
        data = s.recv(1024)
        print("recv:",data)
        s.send(data)
        if not data: #如果 没有数据
            s.shutdown(socket.SHUT_WR) #断开连接,销毁客户端连接
    except Exception as ex:
        print(ex)
    finally:
        s.close() #关闭和客户端的访问关闭

if __name__ == '__main__':
    server(8000)
