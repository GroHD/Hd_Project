#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
字符串就是一个有序的字符的集合,用来存储和表现给予文本的信息。
'''
s  = ''#空字符
s1 = "spam's" #双引号和单引号相同
s2 = 's\np\ta\x00m' #转义序列
s3 = """..."""#三重引号字符串块
s4 = r'\temp\span' #Raw字符串
s5 = b'span' #在Python3.0中的字节字符串
s6 = u'span' # 仅在Python2.6中使用的Unicode字符串
s7 = str('This Is String...') #也可以这样定义一个字符串
'''
s+s1 #合并
s ** 3 #重复
s[0] #索引
s[0:3] #分片
len(s) #求长度
'''
"a %s parrot "%(s1) #字符串格式化表达式
"a{0} parrot".format(s1) #Python2.6和Python3.0中字符串格式化方法
s1.find('pa') #字符串方法调用:搜索
s2.rstrip() #移除空格
s3.replace('pa','xx') #替换
s4.split(',') #按参数进行分割
s5.isdigit() #内容测试
s.lower() # 小写
s.endswith('span') #是否以span结束
st = '|'.join(s1) #插入分隔符
print(st)
s1.encode('utf-8') #该字符串使用什么编码
for x in s2: #迭代该字符串
    print(x)

'spam'in s1  #s1中是否存在spam

st1 = [c * 2 for c in s1]  #把字符串里的每个字符*2 然后转换成列表
print('c',st1)

map(ord,s1)


'''
    在3.0中有三种字符串类型:
        1.str 用于Unicode文本
        2.bytes 用于二进制数据
        3.bytearray 是bytes的一种可变的变体 bytearray 类型在Python 2.6及以后的版本中可用,但是在更早的版本就不可用了。

    在2.6unicode字符串表示宽Unicode文本,str字符串处理8位文本和二进制字数据

    在Python字符串中,单引号和双引号字符是可以互换的。之所以使用这两种形式都可以定义字符串,是因为你可以不使用反斜杠转义字符就可以实现在一个字符串中包含其余种类的引号，如上面的s1字符串

    使用转移序列代表特殊字节:
        转移序列让我们能够在字符串中嵌入不容易通过键盘输入的字节。
        字符串常量中字符"\",以及在它后边的一个或多个字符m在最终的字符串对象中会被一个单个字符所代替，这个字符通过转移定义了一个二进制数据
    例:
'''
a = 'a\nb\tc'
print(a)
r'''
 上面的例子中两个字符\n 表示一个单个字符,在字符集中包含了换行字符这个值得字节，类似的序列\t替代为制表符。

 字符串反斜杠字符:
    \\    反斜杠（保留\）
    \'    单引号(保留')
    \"    双引号(保留")
    \a    响铃
    \b    倒退一个字符
    \f    换页
    \n    换行
    \r    返回
    \t    水平制表符
    \v    垂直制表符
    \N{ID} Unicode 数据库id
    \uhhhh Unicode 16位的十六进制值
    \Uhhhhhhhh   Unicode 32位的十六进制值
    \xhh  十六进制
    \ooo  八进制
    \0    Null (不是字符串结尾)
    \other (不转移保留)
'''
r'''
raw 字符串抑制转义：
    有时候为引入转义符传而是用使用的反斜杠的处理会带来一些麻烦。
    例：
        myfile = open('C:\new\text.data','w')
        他们认为这将会打开一个在C:\new 目录下名为text/data的文件。 问题是这里有'\n'它会识别为一个换行符，并且\t 会被一个制表符所替代。结果就是,这个调用时尝试打开一个名为C:(换行)ew(制表符)ext.data的文件.
        上面这个正是使用raw字符串所要解决的问题。如果字幕r(大写或小写)出现在字符串的第一个引号前面,它将会关闭转义机制。
        myfile = open(r'C:\new\text.data','w')

'''

'''
    三重引号编写多行字符串块：
Python里有一种三重引号内的字符串常量格式,有时候乘坐块字符串,这是一种对编写多行文本数据来说很便捷的语法，并紧跟任意行数的文本,并且以开始时的同样的三重引号结尾
三重引号字符串常量用于文档字符串,他们往往是可以作用多行注释,三重引号也可以使用raw转义字符
'''
#索引切片
r'''
    在Python中字符串的偏移量是从0开始的，并比字符串的额长度小1。Python还支持类似在字符串中使用负偏移这样的方法从序列中获取元素，将负偏移可以看作是从结尾处反向计数
'''
#例:
st2 = 'spam'
print(st2[0],st2[-1])  #得到的结果是 s  m  -1 就是从字符串的尾部开始偏移量为1的元素
print(st2[0:2],st2[1:-2]) #切片字符串,[开始:结束] 返回新字符串,包含开始,但是不包含结尾,

'''
  索引 st2[i] 获取特定偏移的元素:
    第一个元素的偏移为0
    负偏移索引意味着从最后或右边反向进行技术
    st2[0] 获取了第一个元素
    st2[-2] 获取了倒数第二个元素(类似于st2[len(st2)-2]一样)
  分片 (st2[i:j) 提取对应的部分作为一个序列:
    上边界(j) 并不包含在内
    分片的边界默认为0和序列的长度，如果没有给出的话
    st2[1:3] 获取从偏移量为1的元素,直到但不包括偏移为3的元素
    st2[1:] 获取从偏移量为1直到末尾之间的元素
    st2[:3] 获取了从偏移为0直到但是不包括偏移为3之间的元素
    st2[:-1] 获取了从偏移为0直到但是不包括最后一个元素之间的元素。
    st2[:]获取了从偏移0到末尾之间的元素,这有效地实现顶层st2拷贝
    上面最后一个它实现了一个完全的顶层的序列对象的拷贝,一个有相同值,但是是不同内存片区的对象。

  扩展分片L第三个限制值：
    在Python中,分片表达式有一个可选的第三个索引,用作步进。步进添加到每个提取的元素的索引中，完整的形式的分片现在变成了X[I,J,K]，这表示“索引X对象中的元素,偏移为I直到便宜为J-1，每隔K元素索引一次”
    第三个限制---K，默认为1，这也就是通常在一个切片中从左至右提取每一个元素的原因。
例如:
    X[1:10:2]会提取出X中偏移量为1~9之间,间隔了一个元素的元素,也就是手机偏移值为1,2,5,7,9之处的元素。
    X[::2]会取出序列从头到尾每个一个元素的元素
  可以通过一个负数进步，两边界的意义实际上进行了反转，也就是说分片S[::-1]可以把S整个序列进行反转。
'''
#例：
st3='123456789'
print(st3[::-1]) #输出987654321


r'''
    字符串代码转换:
        同样是转换,单个的字符也可以通过将其传给内置的ord函数转换为其对对应的ASCII码,这个函数实际上返回的是这个字符串在内存中对应的字符的二进制
        而chr函数将会执行相反的操作,获取ASCII码并将其转化为对应的字符:
'''
#例:
ch = 'a'
print("ord(C)IS ascii =>",ord(ch))

print("chr(97) Is Chars =>",chr(97))
r'''
    对于单个字符来说可以通过调用内置函数int 可以将单个字符串换为整数（字符串必须是数字,如果字符串内部有其他字符则报错,但个字符无所谓!）：
    int('5')
    >>5
    >>ord('5')-ord('0')

'''
'''
    字符串方法:
'''
strAttr="This String Is Attr"
print(strAttr)
#修改字符串,在字符串中添加一段字符串
upStr = strAttr[:3]+'_NewStr_'+strAttr[3:]
print(upStr)

#替换字符串,replace 方法比这一段代码所表现的更具有普遍性。进行的是全局搜索并替换,第三个参数是替换几个位置的字符,默认是全部。
replaceStr = upStr.replace('_','@@',1)
print(replaceStr)

#可以使用find 进行查找对应的字符串,只会查找一个字符串
index = upStr.find('t')
tr = upStr[:index]+'T'+upStr[index:]
print(tr)

#list 可以将字符串转成成列表
L = list(upStr)
print(L)
L[4]= '&'
#修改之后可以使用字符串方法join 将列表"合成"一个字符串,join将列表字符串连载一起,并用分隔符隔开。下面的这个例子是使用一个空的字符串分隔符将列表转换为一字符串。
upStr = ''.join(L)
print(upStr)

#使用split 对字符串进行分割,返回的是一个列表,分割方法以参数字符为准。默认的是空格进行分割
line = '1aaa bbb ccc      1'
cols = line.split(' ')
print(cols)
#删除结尾或开头的1,默认是删除空格
print(line.rstrip('1'))
#把字符里的字符转换成大写
print(line.upper())
#判断该字符串是否是纯字母的字符串
print(line.isalpha())
#判断字符串是否以1结尾
print(line.endswith('1'))
#判断字符串是否以1开头
print(line.startswith('1'))

r'''
    字符串格式化表达方式:
        Python在对字符串操作的时候定义了%,在字符串中%提供了简单的方法对字符串的值进行格式化,这一操作取决于格式化定义的字符串。
    格式化字符串:

'''
st = 'this is %d %s bird!' % (1, 'Test')
print(st)
'''
    在上面的例子中,1 替换掉了左侧位置中的%d 而'Test'则替换掉了左侧位置的%s
'''

'''
    高级字符串格式化表达式：

        s   字符串
        r   s,但使用repr,而不是str
        c   字符
        d   十进制(整数)
        i   整数
        u   无符号
        o   八进制整数
        x   十六进制整数
        X   大写的十六进制整数
        e   浮点指数
        E   大写的指数
        f   浮点数十进制
        F   浮点数十进制
        g   浮点e或f
        G   浮点E或F
        %   常量%

        在格式化字符串中,表达式左侧的转换目标支持的多种转换操作,有些操作自由一套相当严谨的语法,转换目标的通用结构看上去是这样的:
            %[(name)][flags][width][.precision] typecode
        在%个字符码之间,可以进行以下的任何操作:
                            左对齐(-),正负号(-)和补零（0）的标志位
            给出数字的整体长度和小数点后的位数等。

        x = 123
        res = "intergers:...%d...%-6d...%06d"%(x,x,x) #实现的是默认,6位左对齐,6位补0操作

'''

'''
    基于字典的字符串格式化:
        字符串的格式化同时也允许左边的转换目标来引用右边字典中的键来提取对应的值
        例:
            '%(n)d%(x)s'%('n':1,'x':'span')
            输出结果
                '1 span'

        当字典用一个格式化操作的右边时,它会让格式化字符串通过变量名来访问变量。
'''

food = 'span'
age=40
print(vars()) #那当当前类里所有的变量和参数
print('%(food)s Is %(age)d'%(vars()))

'''
    在新版本中,新的字符串对应的format方法使用主题字符串作为模板,并且接受任意多个表示将要根据模板替换的值的参数。
    在主题字符串中,花括号通过位置(如{1})或关键字(如{food})指出替换目标及将要插入的参数
'''
#例:
template='{0},{1} and {2}'
print(template.format('First','last',3))

template='Name is {name} age is {age} gender is {gender}'
print(template.format(name='hd',age=22,gender='man'))

template ='name Is {name} age is {0} gender is {1}'
print(template.format(22,'man',name='hd'))

r'''
    文件中打包二进制数据的存储和解析:
        Python的标准库中包含一个能够在这一范围起作用的工具：
            struct模块能构造并解析打包二进制数据,它能够把文件中的字符串解读为二进制数据。
            要生成一个打包的二进制数据文件,用'wb'模式打开它,并将一个格式化字符串和几个Python对象传给struct。这里用的格式化字符串是指一个4字节整数，一个包含4个字符的字符串以及一个2位数的数据包，所有这些都按照高位在前的形式。
'''
import struct

with open('data.bin','wb') as file:
    data = struct.pack()

r''''
    string.h里的函数
       string模块里的两个函数:
            1.capwords()
                该函数的作用是将一个字符串中所有单词的首字母大写
                    例:
                        import string
                        s = ' The quick brown for'
                        print(string.capwords(s))
                        输出:
                            The Quick Brown For
            2.maketrans()
                该函数将创建转换表，可以用来结合translate()方法将一组字符串修改为另一组字符,这种做法比反复调用replace()更为高效
                    例:
                        import string
                        leet = string.maketrans('abegiloprstz','463611092572')
                        s = 'Teh quick brown fox jumped over the lazy dog.'
                        print(s)
                        输出:
                            Th3 qu1ck 620wn f0x jum93d 0v32 7h3 142y d06.
                        在上面的李子中,一些字幕被替换为相应的数字
    string模块里的模板:
        字符串模板已经作为python2.4中的一部分,并得到扩展,成为替代内置拼接语法的一种候选方法。
        在使用string.Template拼接时,可以在变量名前面加上前缀$(如$var)来标识变量,或如果需要与两侧的文本框区分,还可以用大括号将变量括起来（如${var}）
            例:
                import string
                varlues = {'var':'food'}
                t = string.Template("""
                    Variable    :$avr
                    Escape      :$$
                    Variable in text :${var}iable
                                    """)
                print('TEMPLATE:',t.substitute(values))
                 输出的结果:
                    TEMPLATE:
                    Variable    :foo
                    Escape      :$
                    Variable in text    :fooiable
                    
                s = """
                    Variable    :%(var)%
                    Escape      :%%
                    Variable in text    :%(var)%iable
                """
                print('INTERPOLATION:'s%values)
                输出结果:
                    INTERPOLATION:
                        Variable    :foo
                        Escape      :%
                        Bariable in text : fooiable
                在上面的两种情况下,触发器字符($或%)都要写两次来完成转义
                
            模板与标准字符串拼接的一个重要的区别,既模板不考虑参数类型。值会转换为字符串，再将字符串插入到结果中。
            在模板中如果value中没有对应的变量名值得时候,substitute()方法会产生一个KeyError的错误。不过safe_substitute()方法不会抛出这个错误,它将错误捕获，并在文本中保留变量的表达式
            
        高级模板:
            高级模板是可以在string.Template的默认语法,为此要调整它在模板中查找变量名所使用的正则表达式,一种简单的做法就是修改delimiter和idpattern类属性
                例:
                    import string
                    template_text="""
                                Delimiter :%%
                                Replaced  :%with_underscore
                                Ignored   :%notunderscored
                                  """
                    d ={
                        'with_undersocre':'replaced',#改变定界符
                        'notunderscored':'not replaced'  #改变替换规则
                        }
                    class MtTemplate(string.Template):
                        delimiter ='%'
                        idpattern ='[a-z]+_[a-z]+'
                    t = MyTemplate(template_text)
                    print(t.safe_substitute(d))
                在上面的例子中,替换规则已经改变，定界符是%而不是$,另外变量名必须包含一条下划线。模式%notunderscored未得到替换,因为其中不包含下划线字符
                上面的打印结果:
                    modified ID pattern:
                        Delimiter:%
                        Replaced : replaced
                        Ignored  : %notunderscored
                要完成更负责的修改,可以覆盖pattern属性,定义一个全新的正则表达式。他提供的模式必须包含4个命名组，分别对应转移定界符，命名变量，用大括号括住的变量名，以及不和的定界符模式。
                    import
                    t = string.Template('$var')
                    print(t.pattern.pattern)
                    t.pattern 是一个已编译的正则表达式,不过可以通过其pattern属性得到原来的字符串表示
                 下面修改自己的一个例:
                    import re
                    import string
                    class MtTemplate(string.Template):
                        delimiter="$" #这里也可以使用自定义的定界符 {{.}},$,%,^,&,@等等都可以
                        pattern="""
                                \$(?:
                                    (?p<escaped>\$)|
                                    (?p<named>[_a-z][_a-z0-9]*)$|
                                    {(?p<braced>[_a-z][_a-z0-9]*)}$|
                                    (?p<invalid>)
                                    )
                                """
                        t = MyTemplate("""
                                        {{
                                        $var$
                                        """)
                        print('MATCHED:',t.pattern.findall(t.template))
                        print('SUBSTITUTED:',t.safe_substitute(var='replacement'))
                        named和braced模式必须单独提供,尽管它们实际上是一样的运行这个例子程序会生成一下结果:
                            MATCHED:[('$','','',''),('','var','',,'')]
                            SUBSTITUTED:
                                {{
                                    replacement
        正则表达式:
            查找文本中的模式:
                re催常见的用法就是搜索文本中的模式。search()函数取模式和要扫描的文本作为输入，如果找到这个模式则返回一个Match对象。如果为找到模式，search()将返回None.
                每个Match对象包含有关匹配性质的信息，包括元输入字符串，使用的正则表达式，以及模式在原字符串中出现的位置
                例：
                    import re
                    pattern = 'this'
                    text = 'Does this text match the pattern?'
                    math = re.search(pattern,text)
                    s = match.start()
                    e = match.end()
                    print('Found "%s"\n in "%s"\nfrom %d to %d ("%s")'%((match.re.pattern,match.string,s,e,text[s:e]))
                    输出结果是:
                        Found "this"
                        in "Does this text match the pattern?"
                        from 5 to 9 ("this")
                    start()和end()方法可以给出字符串中的相应碎银，指示与模式匹配的文本在字符串中出现的位置。
            多重匹配：
                findall()函数会返回输入中与模式匹配而不重叠的所有子串
                例:
                    import re
                    text='abbaaaabbbbbaaaa'
                    pattern='ab'
                    for match in re.findall(pattren,text):
                        print('found"%s"'%(match))
                    这个输入字符串有两个sb子串
                        found 'ab'
                        found 'ab'
                    finditer()函数会返回一个迭代器,它将生成Match实例，而不是Findall()返回字符串
                    import re
                    text = 'abbbbabbbbbaaa'
                    pattern='ab'
                    for match in re.finditer(pattern,text):
                        s = match.start()
                        e - match.end()
                        prin("found"%s" at %d:%d"%(text[s:e],s,e))
                    这个例子找到ab的两次出现，Match实例显示出它们在原输入字符串中的位置。
                    Found "at" at 0:2
                    Found "at" at 5:7
        
                    
                    
'''