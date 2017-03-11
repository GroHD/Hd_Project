#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
 Python的select()方法直接调用操作系统的IO接口,它监控sockets,open,files和pipes方法的文件句柄何时变成readata和writeable或者通信错误,
 select异步IO模型() 使得同时监控多个连接变得简单,并且比写一个长循环来等待和监控多客户端连接要高效，因为select直接通过操作系统提供的C的网络接口进行操作,而不是通过Python的解析器。
 select异步IO模型() 方法接受并监控三个通信列表,第一个是所有的输入的data,第二个是输出的data,第三个是错误的data
'''
#例：
import socket,select,sys
import queue

def Server():
    addrePoint=('0.0.0.0',8000)
    server = socket()
    server.setblocking(0) #设置为非阻塞
    server.bind(addrePoint)
    server.listen(1000)
    message_queues={} #创建消息队列
    inputs =[server] #把server的socket传入input,让select 进行监控
    outputs = []


    while inputs:
        '''
            #当把inputs,outputs,exceptional(这里和inputs公用)传给select()后,它返回三个list,分别是readable，writeable,exceptional
            #所有在readable list中的socket 连接代表有数据可以接受recv,所有在writeable list中存放着你可以对其进行发送(send)操作的socket连接
            #当连接通信出现error时会把Error 信息写到exceptional列表中
    '''
    readable,writeable, exceptional =  select.select(inputs, outputs, inputs,2) #最后一个参数是超时多长时间没有访问就不阻塞
    for s in readable:
        if s is server:#如果serverf存在readable 代表有一个新的连接
            connection,client_addreass=s.accept() #接受到新的链接
            connection.setblocking(False)
            inputs.append(connection)#把新链接放到inputs里
            message_queues[connection] = queue.Queu() #创建该链接的消息队列
        else:#代表客户端连接,可以进行接受和发送数据,有数据进来
            data = s.recv(9128)
            if data:
                print("client recv Mess:%s"%(data))
                message_queues[s].put(data)#消息放入队列等待发送回去
                if s not in outputs: #把客户端放入outputs里等待空闲时间的时候进行发送数据
                    outputs.append(s)
            else:#没有接受到发送回来的数据
                print("client recv no data...")
                #客户端连接断了,从inputs和outpus进行删除
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                del message_queues[s] #把客户端从消息队列中移除
                s.close() #关闭链接
    for s in writeable:
        try:
            next_mes = message_queues[s].get_nowait() #异步取出消息
        except queue.Empty as emp:
            print("output queue fot",s.getpeername(),'is empty')
            outputs.remove(s) #不存在消息队列则从输出列表中移除该链接
        else:
            print("send %s to %s"%(next_mes,s.getpeername()))
            s.send(next_mes)
    #客户端断开之后就会返回这个错误
    for s in exceptional:
        print("client error ",s.getpeername())
        inputs.remove(s) #从inputs 列表中移除
        if s in outputs: #从output 列表中移除
            outputs.remove(s)
        s.close()
        if s in message_queues:
            del message_queues[s] #从队列中移除消息队列
'''
   readable list中socket可以有3种可能的状态,第一种是如果这个socket是main"server"socket,它负责监听客户端的链接,如果这个socket出现在readable中,那代表这是server端已经ready来接受一个新的客户端链接进来
   为了让main sercer 同时能处理多个连接,可以把main server 的socket 设置为非阻塞的模式(blocking)

'''

r'''
    epoll = select.epoll()
'''




