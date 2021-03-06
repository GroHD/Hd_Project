#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
2017-02-28 11:23:20
HD
文件练习学习
    文件对象是Python代码对电脑上外部文件的主要接口,虽然文件是核心类型,但是它有些特殊:没有特定的常量语法创建文件,要创建一个文件对象，
    需要调用内置的open函数,以字符串的形式传递给它一个外部文件名以及一个处理模式的字符串

    例:
        f = open('data.txt','w')#以只读方式打开一个文件
        f.write('hello \n')  #写入一句话并换行
        f.write('word \n')#写入一句话并换行
        f.close()#关闭文件

    上面就是一个简单的打开文件,写入内容并且关闭文件的一个简单例子
'''

f = open('file.txt','w') #以写入的方式打开一个文件,如果文件不存在则创建一个新的文件
f.write("Hell \n")
f.write("Word \n")
f.close()

f = open('file.txt','r') #以读的方式打开一个文件,如果文件不存在则报错,如果不写第二个参数则默认的是读取方式
txt = f.read()#读取内容
print(txt)
f.close() #关闭文件


'''
    文件对象提供了多种读和写的方法,read可以接受一个字节大小的选项,readline每次读取一行等，以及其他的工具seek移动到一个新的文件位置。
    读取一个文件的最佳方式就是根本不读取它,文件提供了一个迭代器,它在for循环或其他环境中自动一行一行地读取。
    可以使用dir(f) 来查看文件操作对象内部的方法和属性
'''
#文件常用操作:
#打开文件操作
output = open(r'file.txt','w')  #创建输出文件 (w是指写入文件)
input =  open(r'file.txt''r') #创建输入文件(r是指读文件)
input = open(r'file.txt') #和上一行是一样的,默认值是r
#读取文件操作
aString = input.read() #吧整个文件读到一个字符串中
aString = input.read(10)#读取之后的10个字节
aString = input.readline()#读取下一行,包括末尾标识符
aList = input.readlines()# 读取整个文件,返回的是一个列表
#写入文件
output.write(aString) #写入字节字符串到文件
output.writelines(aList) # 把列表内的所有字符串输写入到文件
#其他操作
output.close() #关闭打开文件
output.flush() #把输出缓存区刷到硬盘里，但不关闭文件
input.seek(10)#修改文件指针位置到偏移量N处以便进行下一个操作
#迭代
for line in input: #文件迭代器一行行的读取
    print(line)

#其他
open('data',encofing='latin-1')
open('data','rb') #读取一个二进制文件

'''
 打开一个文件的时候程序会调用内置open函数,该函数胡第一个参数是文件名，第二个参数是处理模式。
     r代表为输入打开文件（默认）
     w带表为输出生成并打开文件
     a代表在文件尾部追加内容而打开文件
 在模式字符串尾部加上b可以进行二进制数据处理  rb,wb ab
 在模式字符串尾部加上+ 意味着同时输入和输出文件，也就是说我们可以同时对文件进行读写操作

open 方法要打开的两个参数必须都是Python字符串,第三个参数是可选的,它能够用来控制输出缓存：传入0意味着输出无缓存（写入刚发调用时立即传给外部文件）

如果传入的文件名没有目录路劲时，而那件就默认存在当前工作目录中

'''
r'''
    文件迭代器是最好的读取行工具
        从文本读取文字行最佳的办法就是根本不要读取该文件。而是使用文件迭代器读取内容
    加上"+"意味着同时可以进行输入和输出打开文件,也就是说可以对相同文件对象进行读写,往往与对文件中的修改和超找操作配合使用
    例;
        file = open('str.txt','r+')# 对文件进行读写操作

'''
r'''
      当读取一个二进制数据文件的时候,会得到一个Bytes对象
'''
#例:
data = open('data.bin','rb').read()#以读二进制的方式打开文件data.bin,并读取文件里的全部内容返回到data变量里
r'''
    二进制文件不会对数据执行任何未行转换,在根据转化写入和读取并且实现Unicodeinman的时候,文本文件默认地把所有形式和\n之间映射起来.
'''

r'''
    文件上下文管理:
        文件上下文管理器比文件自身多了一个异常处理功能,它允许我们把文件处理代码包装到一个逻辑层中,以确保在退出后可以自动关闭文件,而不是依赖于垃圾收集上的自动关闭:

            with open(r'c:\misc\data.txt','r') as file:
                for line in file:#迭代器
                    #处理代码





'''