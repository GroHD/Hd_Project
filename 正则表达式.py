r'''

python 中的正则表达式

import  re  #引入正则的包

rem = re.match('正则内容',匹配的数据)  #match 是从开头匹配,无法匹配正文里的数据
print(rm.group())#如果匹配不上则返回的是NONE  

m = re.findall('正则内容',配置的数据)#这个是匹配字符串中的所有数据
print(m) #返回的是一个数组列表。

m = re.search('正则内容','要查询的数据') #查找整个要查询的数据,然后找到第一个需要匹配的内容
print(m.group())
m = re.sub('正则表达式','要替换成什么','要替换的内容',count) #  根据正则表达式替换对应的数据第二个参数是要替换成什么,第三个是替换的内容,第四个是替换第几个,这个替换式不可以从后向前替换的
print(m)
p = re.compile('要匹配的正则内容')
m = p.match(要匹配的内容)
print(m.group()) #上班的内容是提前对要匹配的格式进行了便宜,匹配的时候就不用在编译匹配的格式了, 其它的写法是每次匹配的时候都要进行一次匹配公式的便宜,如果要从一个5W行的文件中匹配某些数据,建议把正则公式先进行编译在匹配。
m =re.split('正则表达式','匹配的内容')
#按正则表达式进行匹配,然后返回该数组

表达式内容：
[0-1]  匹配数字
{n,m} 匹配n到m个
{a-zA-Z} 匹配A-Z 的大小写
. 匹配一个
.+匹配多个

* 匹配0个或多个
[^XXX]  匹配除了XXX
\s 匹配任意非空字符
\W 匹配非字母数字
\S 匹配非空的任意字符
\d 匹配任意数字

^XX 以XX开头
$XX以XX结尾
|  或  A|B  匹A或B

正则表达式匹配糗事百科文字信息:
file = open('index.html','r',encoding='utf-8')#读取数据
strNum = file.read() #读取数据
file.close()#关闭文件
#print(strNum)
reMatch = "<div class=\"content\">*+</div>"
m = re.findall('<div class="content">[.|\n]*<span>(.*)</span>[.|\n]*</div>',strNum)
for i in m:
    print(i)
'''