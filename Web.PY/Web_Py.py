#!/usr/bin/env python
#-*- coding:utf-8 -*-
r'''
    需要引入web.py包 
    2017年10月26日15:37:00  这个时候似乎web.py 还不支持python3.X

'''
import web
#设置url的静态配置
urls = ('/','hello')
#要访问的Models
class hello(object):
    def GET(self):
        return "Hllo Word"
#启动函数
if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()