#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
'''
Socket:
    Socket 通常称作"套接字",用于描述IP地址和端口,是一个通信链的句柄。

'''
ip_port = ('127.0.0.1',8811)
sk = socket.socket()
sk.setblocking(False)# 设置不Socket不阻塞,现在不论send是否发送成功都不会阻塞,recv无论是否有数据也不会阻塞,True或False
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
        Socket常用语法:
            Socket Families(地址簇)
                soekct.AF_UNIX  unix本机进程间通信
                socket.AF_INET IPV4   服务器之间网络通信
                socket.AF_INET6 IPV6  
             Socket Types  Socket 类型
                socket.SOCK_STREAM  tcp
                socket.SOCK_DGRAM upd
                socket.SOCK_RAW  原始套接字,普通的套接字无法处理ICMP,IGMP等网络报文,而SOCK_RAW 则可以,
                                 其次,SOCK_RAW也可以处理特殊的IPv4报文，此外，利用原始套接字，通过IP_HDRINCL套接字选项可以构造用户IP头
                                 
                socket.SOCK_RDM  #是一种可靠的UDP形式,既保证交付数据,但是不保证顺序,SOCK_RDM用来提供对原始协议的低级访问，
                                  在需要执行某些特殊操作时，如发送ICMP报文。
                socket.SOCK_SEQPACKET #可靠的连续数据包服务，已很少使用
                

        socket 方法：
            socket.soekct(famil=FA_INET,type=SOCK_STREAM,proto =0,fileno=None) #创建方法的时候默认的参数，ip4 和tcp服务
            socket.socketpair([famils[,type[,prote]]])
            socket.create_connection(address[,timeout[,source_address]])
            sk.bind(address) 绑定ip地址和端口号,address地址的格式取决于地址簇，在AF_INET下,以（host，port）的形式表示地址
            sk.listen(backlog) 最多等待几个，backlog 制定在拒绝链接之前,可以挂起的最大连接数量，backlog等于5，表示内核已经接到了链接请求,但服务器还没有调用accept进行处理的链接数,这个值不能无限大,因为要在内核中维护链接队列
            sk.setblocking(bool) 是否阻塞(默认TRUE)，如果设置False,那么accept和recb时一旦无数据,则报错
            sk.accept()  接受链接并返回(conn,address),其中conn是新的套接字对象,可以用来接收和发送数据,address是连接客户端的地址,接受TCP客户的连接（阻塞式）,等待链接的到来,如果一直没有客户端访问,则该方法一直在阻塞
            sk.connect(address) 连接到address处的套接字,一般,address的格式为元祖(hostName,port),如果链接出错,返回socket.error错误,该方法是客户端使用的
            sk.connect_ex(address) 同上,只不过会有返回值,链接成功时返回0,链接失败时候返回编码,例如：10061
            sk.close() 关闭套接字
            sk.recv(bufsize[,flag]) 接受套接字的数组,数据以字符串形式返回,bufzise指定最多可以接受的数量,flag提供有关消息的其他信息,通常忽略的
            sk.recvfrom((bufsize[,flag]) 与recv()类似,但返回值是(add,address),其中data是包含接受数据的字符串,address是发送数据的套接字地址
            sk.send(string[,flag]) 将string 中的数据发送到链接套接字，返回值是要发送的字节数量，该数量可能小于string的字节大小。既:可能未将制定内容全部发送。
            sk.sendall(string[,flag]) 将string中的数据发送到连接的套接字,但在返回之前会尝试发送所有数据。成功返回None,失败则抛出异常。该方法一般是服务器使用
            sk.sendto(string,[flag],address) 将数据发送到套接字,address是形式为(ipaddr,port)的元祖,返回值是发送的字节数,该函数主要是用于UDP协议。
            sk.settimeout(timeout) 设置套接字操作的超时时间,timeout是一个浮点数,单位是秒。值为None表示没有超时期。一般，超时期应该在创建套接字时设置,因为它们可能用于连接的操作。
            sk.getpeername() 返回链接套接字的远程地址。返回值通常是元祖(ipaddr,port)
            sk.getsockname() 返回套接字自己的地址,通常是一个元祖(ipaddr,port)
            sk.getsockopt(level,optname[.buflen]) 返回套接字选项的值
            sk.gettimeout() 返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None
            sk.fileno() 套接字的文件描述
            sk.sendfile(file,offset=0,count=None) 发送文件,该方法是新版本里才有的。似乎在目前版本里无用
            
    '''