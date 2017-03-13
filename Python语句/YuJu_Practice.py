#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
    Python 的语句:

        语句          角色                  例子

        赋值          创建引用值            a,b,c = 'good','bad','ugly'

        调用          执行函数              log.write('spam,ham')

        打印调用       打印对象              print('这是打印数据','hd')

        if/elif/else  选择动作            if 'spam' in text:
                                            print(text)

        for/else      序列迭代            for x in mylist:
                                            print(x)

        while/else    一般循环            while x > y:
                                            print("Hello")

        pass           空占位符           while True:
                                            pass

        break          循环退出           while True:
                                            if exittest():break

        continue       循环继续           while True
                                            if skiptest(): continue
        def            函数和方法         def  f(a,b,c=1,*d)
                                            print(a+b+c+d[0])
        return         函数结果           def  f(a,b,c=1,*d):
                                            return a+b+c+d[0]
        yield          生成器函数         def gen(n):
                                            for i in n:yield i*2

        global         命名空间           x = 'old'
                                        def function():
                                            global x,y; x = 'new'
        nonlocal       Namespaces(3.0+) def outer():
                        命名空间(Py3.0以上)   x = 'old'
                                            def function:
                                                    nonlocal x;x = 'new'

        import        模块访问             import  sys

        from          属性访问             from sys import stdin

        class         创建对象             class Subclass(Superclass):
                                                staticData=[]
                                                def method(self):pass

        try/except/finally   捕获异常       try:
                                                cation()
                                           except:
                                                print('action error')

        raise        触发异常               raise EndSearch(location)

        assert       调试检查               assert x>y,"X too small"

        with/as      环境管理器              with open('data') as myfile:
                                                print(myfile)

        del          删除引用                del data[k]
                                            del data[i:j]
                                            del obj.attr
                                            del variable

'''