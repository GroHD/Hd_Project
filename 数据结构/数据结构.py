#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
import collections
r'''
    python 包含很多标准变成数据结构,如 list,tuple,dict,set,这些都属于其内置类型。对很对应用来说这些结构已经足够了，不在需要其他类型。
    
collections ----   容器数据类型
    collections模块包含除内置类型list,dict和tuple以为的其他容器数据类型
    Counter
     Counter作为一个容易,可以跟踪相同的值增加了多少次。这个类可以用来实现其他语言中常用包或集合包数据结构来实现的算吗。
    Counter支持3种形式的初始化。调用Counter的构造函数时可以提供一个元素序列或者一个包含键和技术的字典，还可以使用关键参数将字符串名映射到计数。
        import collections
            print(collections.Counter(['a','b','c','a','b','b']))
            print(collections.Counter({'a':2,'b':3,'c':1}))
            print(collections.Counter(a=2,b=3,c=1))
            上面这三种形式的初始化结果都是一样的。
        如果不提供任何参数,可以构造一个空Counter,然后通过update()方法填充
        import collections
            c = collections.Counter()
            print(c) #这个打印出来就是一个空的
            c.update('abcdaab')
            print('update Counter():',c) #打印出更新后的数据 Counter({'a':3,'b':2,'c':1,'d':1})
            c.update({'a':1,'d':5})
            print('update Counter():',c)#打印出更新后的数据 Counter({'a':4,'b':2,'c':1,'d':d})
        访问计数:
            一旦填充了Counter,可以使用字典API获取它的值。
            import collections
            c = collections.Counter('abcdaab')
            for letter in 'abcde':
                print('%s:%d',%(letter,c[letter]))
                #对于未知的元素,Counter不会产生KeyError。如果在输入中没有找到某个值(比如上面例子中的e)，其计数是0.
            可以使用elements()方法返回一个迭代器，将生成Counter知道的所有元素集合(list)
            import collections
            c = collections.Counter('abcdefgabcd')
            c['z'] = 0
            print(c)#打印出的结果是 Counter(('a':2,'b':2,'c':2,'d':3,'e':1,'f':1,'g':1,'z':0))
            print(list(c.elements()))#使用elements()函数，不能保证元素的顺序不变,而且技术小于或等于0的元素不包含在内
            ['a','a','b','b','c','c','d','d','e','f','g']
            使用most_common()函数可以生成一个序列,其中包含n个最常遇到的输入值及其相应技术。
            import collections
            c = collections.Counter('aabbddlll,qqq,rrr')
            for letter,count in c.most_common(3):
                print('%s : %d\n'%(letter,count))
            上面的例子要统计输入的值中所有出现的字母来生成一个频度分布，然后打印3个最常用的字母，如果不向most_common()函数提供参数,会生成由所有元素构成的一个列表，按频度排序
            输出结果:
                llll:4
                qqq:3
                rrr:3
                
    defaulddict：
        标准字典包括一个方法setdefault()来获取一个值，如果这个值不存在则建立一个默认值。与之相反，default初始化容器时会让调用者提前来制定默认值
        import collections
        def default_facory():
            :return 'default value'
        d = collection.defaultdict(default_facory,foo='bar')
        print('d:',d)
        print('foo=>',d['foo'])
        print('bar=>',d['bar'])
        所有的键都用相同的默认值并无不妥,就可以使用这个方法。如果默认值是用于聚集或累加值的类型，这个方法尤其有用。
        
    deque:
        deque(双向队列)支持从任意一段增加和删除元素。更为常用的两种结构，既栈和队列，就是双向队列的退化形式，其输入和输出限制在一端。
        import collections
        d = collections.deque('abcdefg')
        print('Deque:',q)
        print('Length:',len(d))
        print('Left end:',d[0])
        print('Right end:'d[-1])
        d.remove('c')
        print('remove(c):',d)
        由于deque是一种序列容器,因此同样支持list的一些操作，如用__getitem__()检查内容,确定长度,以及通过匹配标识从序列中间删除元素
        上面输出的结果是:
            deque:deque(['a','b','c','d','e','f','g'])
            Length:7
            Left en : a
            Right end:g
            remove(c):deque(['a','b','d','e','f','g'])
        填充:
            deque可以从任意一端填充,在python实现中称为:"左端"和"右端"
            import collections
            dl = collections.deque()
            #添加右边
            dl.extend('abcdefg') 
            print('extend:',dl)#输出结果：deque(['a','b','c','d','e','f','g'])
            dl.append('h')
            print('append:',dl)#输出结果：deque(['a','b','c','d','e','f','g','h'])
            
            #添加到左侧
            d2 = collections.deque()
            d2.extendleft(xrange(6))  #输出结果 
            print('extendleft:',d2)#输出结果 deque([5，4，3，2，1，0])
            d2.appendleft(6)
            print('appendleftL',d2)#输出结果 deque([6，5，4，3，2，1，0])
            extendleft()函数迭代处理其输入,对各个元素完成与appendleft()同样的处理.最终结果是deque将包含逆序的输入序列
        移除:
            deque可以从两端或任意一端删除元素
            import collections
            d = collections.deque('abcdefg')
            while True:
                try:
                    print(d.pop)#默认从右边删除
                except IndexError:
                    break
            d1 = collection.deque(xrange(6))
            while True:
                try:
                    print(dl.popleft()) #从左边开始删除元素
                except IndexError:
                    break
        
'''