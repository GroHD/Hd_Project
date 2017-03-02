#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
2017-02-28 11:23:20
HD
字典练习学习
    除了列表外,字典也许就是Python之中最灵活的内容数据结构类型。如果把列表看作是有序的对象集合,那么久可以把字典当成无序的集合。他们的主要差别就是字典当中的元素是通过键来存取的,而不是通过偏移量存取的。
字典有以下的属性:
        通过键而不是偏移量来读取
        任意对象的无序集合
        可边长，异构，任意嵌套
        属于可变映射类型
        对象引用表(散列表)
    字典类型名为dict.当携程常量表达式时，字典以一些列"键:值(key:value)" 对形式写出的,用大括号括起来，一个空字典就是一对空的大括号，而字典可以作为另一个字典(列表，元祖)中的某一值被嵌套
'''
#常见字典常量和操作 2017年3月2日11:49:09  新添加
D  = {}  #空字典
D1 = {'soam':2,"eggs":3} #两项目字典
D3 = {'food':{'ham':1,'egg':2}} #嵌套
D2 = dict([('name','hd'),('age',28)])#创建字典
D4 = dict.fromkeys((['a','b']),'Nonn') #其他构建技术，这个只有key　没有value,默认是none,也可以在后面单独设置默认值
print(D4)
D5 = dict(zip(['keys1','keys2','keys3'],['values1',['v','a','l','u','e','s','2'],'values3']))#创建键值对
print(D5)
D6 = dict(name='bob',age=29) #创建对应的键值对
print(D6)
D1['soam']#以键进行搜索运算,不存在报错!
D3['food']['ham'] #以键进行搜索多层嵌套,不存在报错
print("Checked Is egg In Ds:",('egg' in D3)) #判断egg 是否在D3字典键中中存在
D3.keys() #拿到D3的所有key 返回的是一个列表
D3.values() #拿到D3的所有的value  返回的是一个列表
D3.items() #拿到D3字典的键和值 [(k,v),(k,v),...]
D4 = D3.copy() #把D3浅拷贝一份
print("copy:",D4)
obj = D4.get('food1','Noo')#从D4字典中根据key取出对应的数据,如果key不存在则返回默认值(第二个参数)
print("GET:",obj)

D4.update(D1) #把D1合并到D4上去
print("Update:",D4)


Obj1 = D4.pop('eggs')#从D4中拿出eggskey下的vlue值
print("Pop:D4剩余元素:",D4,"取到的值：",Obj1)
D_len = len(D4) #拿到D4的长度(存储的元素的数目)
D4['soam'] = 12 #修改D4某个键下的元素
print("D4 Update :",D4)
D4['Name']='hd' #给D4增加元素
print("D4 Insert:",D4)
del D4['soam'] #根据Key删除个元素
print("Del D4:",D4)
dic_list = list(D4.keys()) #拿到所有D4的键然后转成列表后返回
print("D4 List :",dic_list)

b = 'soam' in D4 #判断D4中是否存在键'soam'

D7 = {x:x*2 for x in range(10)} #生成字典
print("For Create Dict :",D7)



#之前的笔记
rec ={"name":{"first":'HD',"last":"dd"},'job':['dev','msgr'],'age':40.5}
print(rec['name'])#找到name keys 下的value
print(rec['name']['first']) #找到name 下的first keys
print(rec['job']) #找到job 列表
print(rec['job'][-1]) #拿到job 列表里最后一个值
rec['job'].append('janitor') #向job 表里添加数据
print(rec)
#rec = 0 #清理内存对象

print("Keys:",rec.keys()) #拿到字典的keys
print("VALUES:",rec.values()) #拿到字典的Values

#循环输出keys和对应的vlue
for key in rec.keys():
    print(key,"=>",rec[key])

#可以使用sorted 来给字典进行排序
for k,v in sorted(rec.items()):
    print(k,"=>",v)

'''
    字典可以使用列表，元祖，数字当key，类似于的字典键也常用语实现稀疏数据结构。
    例：
        多维数组中只有少数位置上有存储的值：
            Matrix={}
            Matrix[{2,3,4}] = 88
            Matrix[{7,8,9}] = 99
            x = 2,y = 3 , z = 4
            obj = Matrix[x,y,z]
            print(obj)

            print(Matrix)

    避免键不存在的错误：
        读取不存在的键的错误在字典中很常见,可以在if语句中先对键进行测试看是否存在，还可以使用try语句明确地捕获并修复这一异常，还可以使用字典本身的get方法为不错你在键提供一个默认值

'''