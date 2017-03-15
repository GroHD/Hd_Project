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


    在检查一个内容是否是int类型时，可以使用isdigit方法检查字符的内容
    s ='123'
    X = 'XXX'
    s.isdigit()
    X.isdigit()
    (True,False)

Try 语句处理错误:
    在Python中,处理错误最通用的方式就是使用try语句，用它来补货并完全复原错误信息。
    try:
        XXXXX
    except:
        XXXX
    else:
        xxxx

    这个try 语句的组成是：try 关键字后面跟代码主要代码块（XXXXX），在跟except 部分，给异常处理代码（XXXX），再接else 部分，如果try部分没有引发异常
    就执行这一部分代码,ptyhon 会先执行tyr 部分, 如果有异常就运行except部分或没有异常执行else部分
'''

r'''
赋值语句形式：
    spam = 'Spam' 基本形式
    spam,ham = 'yum','YUM'  元祖赋值运算(位置性)
    [spam,ham] = ['yum','YUM'] 列表赋值运算(位置性)
    a,b,c,d = 'spam'  序列赋值运算,通用性
    a,*b = 'spam' 扩展的序列解包   一种新的序列赋值允许我们更灵活地选择要赋值的一个序列部分, 等号右边的s赋值给等号左边的a，b赋值给pam 这为手动分辨操作的结果的赋值提供了一种简单的替代方法
    spam = ham = 'lunvh' 多重目标赋值运算   变量名spam和ham两者都赋值成相同的字符串对象'lunch'的引用，效果和写成ham ='lunch' 然后在写spam =ham。
    spams += 42  增强赋值运算(相当于spams = spams+42)

    注意虽然可以在等号两侧混合相匹配的序列类型，右边元素的数目还是要跟左变变量的数目相同，不然会产生错误。
    a,b,c,d = 'abcd'#正确
    a,b,c,f = 'abc' #错误,等号两遍就的数量不同

    要是想通用的话，就需要使用分片了，这里有几种方式使用分片运算，可以使最后的情况正常工作。

    a,b,c = sting[0],sting[1],sting{2:]




'''