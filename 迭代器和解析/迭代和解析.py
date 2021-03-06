#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
    在pyhthon中for循环用以用于任何序列类型,包括列表，元祖以及字符串:
        for x in [1,2,3,4,5]:
            print(x**2,end='')
    
    文件迭代器:
        在文件中，有一个方法,名为__netxt__就是一个迭代器,每次调用时,就返回文件中的下一行。当到达文件末尾时,__next__会引发内置的StopIteration异常,而不是返回空字符串
        
        例:
            f = open('file.txt','r')
            f.__next__()
            f.__next__()
            
            raise StopIteration()
            #如果不存在就返回一个异常StopIteration
            
        __next__()就是python中所谓的迭代协议:
                有__next__方法的对象会前进道下一个结果,而在一系列结果的末尾时，会引发StopIteration异常。
                在python中任何类对象都认为是可迭代的。任何类对象也能以for循环或其他迭代工具便利,因为所有迭代工具内部工作起来都是在每次迭代中调用__next__(),并且捕捉StopIteration异常来确定何时离开循环。
                
'''
r'''
    为了支持手动迭代代码,python3.0还提供了一个内置函数next,它会自动调用一个对象的__next__方法,给定一个可迭代对象X,调用next(X)等同于X.__next__(),但前者简单很多。
    
    因为列表以及很多其它的内置对象,不是自身的迭代器,因为他们支持多次打开迭代器,对这样的对象,我们必须调用iter来启动迭代:
        L=[1,2,3]
        b = iter(L) is L
        print(b) #打印结果False
        L.__next__()#这样会报错,说List 对象没有__next__ 属性
        L = (x **2 for x in range(100)) #生成一个迭代器
        I = iter(L) #把list 转换成迭代器 并返回一个新的对象
        I.__next__()  #返回的结果是1
        netx(I) #返回的结果是2 next(I) 等价于上面的I.__next()__
'''

r'''
    列表解析:
        列表解析卸载一个方括号中,因为它们最终是构建一个新的列表的一种方式。
        例:
            L = [1,2,3,4,5,6]
            L = [x+10 for x in L]
            
            它们以们所组成的一个任意的表达式开始,该表达式使用我们所组成的一个循环变量(x+10)。这后边跟着我们现在应该看做是一个for循环头部的部分，它声明了循环变量，以及一个可迭代对象(for x in L)
            要运行该表达式,python在解释器内部执行一个便利L的迭代，按照顺序把x赋给每个元素,并且手机对个元素运行左边的表达式的结果。
            
        
        如果是在每一个序列中的每一项上都执行某一个特定的操作的时候,都可以考虑使用列表解析。
        
        例如打开一个文件读取文件中所有的内容,我们不用提前打开文件,如果我们在表达式中打开文件,列表解析将自动使用迭代协议。也就是说，它将会调用文件的next方法,每次从文件读取一行。
        
        lines = [line.rstrip() for line in open('file.txt')]
        
    实际上列表解析可以有更高级的应用。作为一个特别有用的扩展，表达式中嵌套的for循环可以有一个相关的if字句来过滤那恶邪测试不为真的结果想。
    例:
         L = [10, 2, 3, 44, 11, 16, 56, 76, 19, 87]
         L = [x for x in L if x < 10 ]
         print(L)
         列表解析中的if语句检查从L列表中读取的每一个元素,看它是否兄啊与10,如果不是从结果列表中省略该元素。
'''
r'''
    其它迭代器:
    Map迭代器:
        def funName(*obj):
        return obj[0]+1
        
        L =[1,2,3,4,5,6]
        L1 = map(funName,L)
        print(list(L1))
        
'''

