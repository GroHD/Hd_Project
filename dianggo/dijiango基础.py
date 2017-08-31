#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
djiango是一种框架,
pip install djiango 
1.创建Djianggo程序
    a. 命令自动创建
        djiango-admin startproject [ProjectName]  创建工程 在ProjectName的问家里有同名的文件夹是配置文件
        python manage.py startapp [appName]  进入ProjectName 文件夹里执行manager.py 创建对应的app  必须使用startapp创建单独的Project
        文件夹路径：
            ProjectName
                ------>ProjectName    ---配置文件,所有项目共享该文件
                ------>manager.py     ---创建Porject文件
                ------>app01          ---使用manager.py创建的项目
                ------>app02          ---使用manager.py创建的项目
            
    b.使用pycharm 创建
            直接创建Django程序
            然后再终端使用  python manage.py startapp [appName]  直接创建
            
    Djiango URL:
         from 导入项目的试图
        可以在项目的配置文件里找到urls.py里进行配置url,这里需要使用正则表达式来匹配
            urlpatterns=[
                    #在这里添加要匹配的url
                    url(r'^articles/2003/$',项目试图里的那个试图的方法),#精确匹配
                    url(r'^articles/([0-9]{4})/$',views.year_archive), #匹配以4个数字为结尾的路由,在方法year_archive 里需要两个参数,第一个是常驻参数request,第二个参数是匹配到的四个数字
                    url(r'^articles/[0-9]{4}/([0-9]{2})/([0-9]+)/$',views.year_archive), #匹配年月开头,一个或多个数字结尾的url
                    url(r'^articles/[0-9]{4}/([0-9]{2})/([0-9]+).php/$',views.year_archive), #匹配以php结尾的url
                    url(r'^articles/[0-9]{4}/.(/w)/$',views.year_archive),#匹配以为任意字符结尾的url
                    #制定匹配名称的正则表达式
                    url(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.year_archive)#在正则表达式里的指定名称(尖括号里的名称), 那么在试图里的时候必须使用这样的名称,否则报错
                    #把请求分发到对应的app里,然后再app里进行配置url
                    url(r'^payment/',include(app01.urls))#所有以payment的请求都跳转到 app01下的Urls进行处理url请求,然后需要在app01文件夹下创建urls 这个路由请求,app01里的urls写法和当前文件写法是一样的
                     #向试图里传参数
                    url(r'^payment/([0-9]{4}/$)',view.FunctionName,{'file_type','json'})#第三个参数是服务器写的,可以向view方法里的file_type参数传入该值,只要访问该Url都会携带该参数。第三个参数可以是动态的传入。
            ]
        #每次匹配都会从列表里挨个进行匹配,匹配到之后就不会向后继续匹配
                  
                  
                  
     Djiango GET和POST提交:
                在view里可以使用request.method=='GET or POST' 来判断提交方式是什么
                request.GET.get('user')  使用GET获取数据
                
                
            
             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
        
'''