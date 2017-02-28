#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class WebServer(object):
    def __init__(self,host,point):
        self.host  = host
        self.point = point

    def start(self):
        print("%s is host %d is Point....Start...."%(self.host,self.point))
    def stop(self):
        print("%s Stop Success...."%(self.host))

#定义一个和类没有关系的方法 ini 就是需要实例调用这个方法的时候传入自己
def test_run(ini,name):
    print("My Name Is %s   Host iS %s"%(name,ini.host))

if __name__ == '__main__':
    server = WebServer('localhost',3333)

    # #判断server类里是否有方法,如果有则返回true  否则返回false
    # if hasattr(server,sys.argv[1]):
    #     #获取某个方法的内存地址
    #     func = getattr(server,sys.argv[1])
    #     func()#执行这个方法

    setattr(server,'run',test_run) #把test_run方法绑定到server类中
    # 执行这个方法, run就是上面绑定的run  这个绑定在其他实例里不会有,其他实例无法使用,
    # 要是在这个方法里想调用类里的属性需要把当前实例传入该方法,第一个参数就是自己
    server.run(server,"hd")
    # 从类里删除某个方法
   # delattr(server,'run')
    #server.run(server,"hd")
    #使用实例对象删除 某个属性
    #delattr(server,'host')
    server.run(server, "hd")

    #使用类删除类里本身的方法
    delattr(WebServer,'start')

    server.start()