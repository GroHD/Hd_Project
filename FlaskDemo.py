#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
# from flask import Flask,request,make_response,redirect,render_template  #request 是Flask使用上下文临时把某些对象变为全局可访问。有了上下文就可以拿到请求头里的数据
# app = Flask(__name__)
#
# @app.route('/')
# def Index():
#     #下面这句话就是拿到请求头里的数据
#     user_agent = request.headers.get('User-Agent')
#     r'''
#         Flask上下文全局变量
#         current-app    当前激活程序的程序实例
#         g              处理请求时用作临时存储的对象,每次请求都会重新设定这个变量，这个变量是全局使用的
#         request        请求对象,封装了客户端发出的Http请求中的内容
#         session        用户会话,用于存储请求之间需要“记住”的值的字典
#     '''
#     r'''
#         Flask请求钩子：
#             before_first_request  注册一个函数,在处理第一个请求之前运行
#             before_request 注册一个函数,在每次请求之前运行
#             after_request   注册一个函数,如果没有未处理的异常抛出,在每次请求之后运行,该注册函数至少需要一个参数，这个参数实际上为服务器的响应，且函数中需要返回这个响应参数
#             teardown_request    注册一个函数,即使有未处理的异常抛出,也在每次请求之后运行，该注册函数至少需要一个参数,这个参数实际上为服务器的响应，切函数中需要返回这个响应参数
#         在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g。如果,before_request 处理程序可以从数据库加载已登陆用户,并将其保存到g.user中,随后调用试图函数时,试图函数在使用g.user获取用户
#         例:
#          使用 @app.before_first_request
#              def StartIndex():
#                   #处理第一个请求之前执行这个代码

#     '''
#     r'''
#         Flask请求响应:
#             Flask调用试图函数后,会将其返回值作为响应的内容。HTTP相应中一个很重要的部分是状态吗,Flask默认设为200,这个状态吗表明请求已被成功处理
#             如果试图函数返回的响应码不一样,那么可以把数字代码作为第二个参数返回值，添加到响应文本之后
#             例:
#             @app.route('/')
#             def index():
#                 return '<p>400错误</p>',400
#             试图函数返回的响应还可以接受第三个参数,这个一个由请求头组成的字典,可以添加到Http相应中。
#
#             如果不想返回由1个，2个或3个值组成的元素,Flask 试图函数还可以返回Response对象,make_reponse()函数可以接受1个，2个或3个参数(和试图函数返回的值一样),并返回一个Response对象。
#             例子：
#                 需要导入:make_response
#                 response = make_respone('<h1>Thos Document a Cookie',200)
#                 response.set_cookie('userName','hd')
#                 return response
#
#             有一种名为重定向的特殊响应类型。这种响应没有页面文档，只告诉浏览器一个新地址用以加载新页面。
#             重定向经常使用302状态码表示，只想的地址由响应体 Location提供。重定向响应可以使用3个值形式的返回值生成，也可以在Response对象中设定，由于使用很频繁，Flask提供了Redirect()函数用于生成这种响应
#             例：
#                 需要导入  redirect
#                 return  redirect('http://www.so.com')
#             还有一种特殊的响应由abort函数生成，用于处理错误。
#             例:
#                 需要导入 abort
#
#                 user = load_user(id)
#                 #如果用户不存在则返回404
#                 if not user:
#                     abort(404)
#                 return '<h1> Hello ,%s' %(user.name)
#                 #这里abort 不会吧控制权交还给调用它的函数，而是抛出异常把控制权交给Web服务器。
#     '''
#     r'''
#         模板:
#             Jinja2模板引擎:
#                 在默认情况下Flask在程序文件夹中的templates子文件夹中寻找模板。
#                 Flask提供的render_template函数把Jinja2模板引擎集成到了程序中,render_template函数的第一个参数是模板的文件名。随后的参数都是键值对，表示模板中变量对应的真实值，
#
#     '''
#     return render_template('index.html')
# @app.route('/user/<name>')
# def HelloName(name):
#     return render_template('user.html',userName=name)
#     r'''
#         变量:
#             在上面的例子中模板使用的是{{userName}}结构表示一个变量，它是一个特殊的占位符，告诉模板引擎这个位置的值从渲染模板时使用的数据中获取。
#             Jinja2能识别所有类型的变量，甚至是一些负责阿德类型，例如:列表，字典和对象。在模板中使用变量的一些示例：
#                 <p>A  value from a dictionary:{{mydict['key']}}</P>
#                 <p>A  value from a list:{{mylist[3]}}</P>
#                 <p>A  value from a list,with a variable index:{{mylist[myintvar]}}</P>
#                 <p>A  value from a object's method:{{myobj.somemethod()}}</P>
#
#             可以使用过滤器修改变量,过滤器名添加在变量名之后,中间使用竖线分割。
#             例:
#                 Hello {{userName|capitalize}}
#
#             Jinja2变量过滤器:
#                 safe    渲染值时不转义
#                 capitalize  把值的首字母转换成大写，其它字母转换成小写
#                 lower   把值转换为小写形式
#                 upper   把值转换成大写形式
#                 title   把值中每个单词的首字母转换成大写
#                 trim    把值得首位空格去掉
#                 striptage   渲染之前把值中所有的html标签都删掉
#              在默认情况下,处于安全考虑,Jinja2会转义所有变量。例如'<h1>Hello</h1> 'Jinja2会将其渲染成 '&lt;h1&gt;....'
#
#             Jinja2控制结构：
#                 Jinja2提供了多种控制结构,可用来改变模板的渲染流程。
#
#                 if流程控制：
#                     {%if user%}
#                         Hello,{{user}}
#                     {%else%}
#                         Hello,Staranger!
#                     {%endif%}
#                 for 循环
#                     <ul>
#                         {%for item in users%}
#                             <li>{{item.userName}}</li>
#                         {%endfor%}
#                     </ul>
#                 Jinja2还支持宏，宏类似于Python代码中的函数：
#                     {% macro render_connent(item)%}
#                         <li>{{item.userName}}</li>
#                     {%endmacro%}
#                     <ul>
#                         {%for item in users%}
#                             {{render_comment(comment)}}
#                         {%endfor%}
#                     </ul>
#                 为了可以重复使用宏，可以将宏保存在单独的文件中,然后再需要使用的模板中导入：
#             自定义错误页面:
#                 像普通路由一样,Flask允许程序使用基于模板的自定义错误页面，最常见的错误代码有两个：404和500错误
#                 @app.errorhandler(404)
#                 def page_not_found(e):
#                     return render_template('404.html'),404
#                 @app.errorhandler(500)
#                 def internal_server_error(e):
#                     return render_template('500.html'),500
#             Flask 链接
#                 Flask提供了url_for()辅助函数,它可以使用程序URL映射中保存的信息生成URL,url_for()函数最简单的用法是以视图函数名(或app.add_url_route()定义路由时使用的端点名称)作为参数,返回对应的Url，
#                 例如在当前页面的程序中调用url_for('index') 得到的结果是/。调用url_for('index',_external=True)返回的则是绝对地址，在这个页面的例子中是http://localhost:500/
#                 使用url_for()函数生成动态地址时,将动态部分作为关键字参数传入。例如:url_for('user',name='hd',_external=True)的返回结果是http://localhost:500/user/hd
#                 传入url_for()的关键字参数不仅限于动态路由中的参数。函数能将任何额外的参数添加到查询字符串中，例如：url_for('index',page=2) 返回的结果是/?page=2
#
#
#
#
#
#     '''
# if __name__ == '__main__':
#     app.run(debug=True)
#
#     r'''
#         Web表单:
#             默认情况下,Flask-WTF能保护所有表单免受跨站请求伪造的工造。恶意网站把请求发送到被攻击者已登陆的其他网站时就会引发CSRF攻击。
#             为了实现CSRF保护,FLASK-WTF需要程序设置一个密钥。Flask-WTF使用这个密钥生成加密令牌,在用令牌验证请求表单数据的真伪。设置密钥的方式如下所示:
#         例:
#     '''
#     app = Flask(__name__)
#     app.config['SECRET_KEY']='!@#$%^ASDKJHGhhqwe!!~~~'
#     r'''
#      app.config 字典可以用来存储框架，扩展和程序本身的配置变量。使用标准的字典句法就能把配置值添加到app.config对象中。
#      SECRET_KEY 配置变量是通用密钥，可在Flask和多个第三方扩展中使用。
#     '''
#
#     r'''
#         表单类:
#             使用Flask_WTF时，每个Web表单都由一个继承自form的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求
#     '''
# from flask_wtf import Form
# from wtforms import StringField,SubmitField
# from wtforms.validators import DataRequired
#
# class NameForm(Form):
#     name = StringField('Whatis your name?',validators=[DataRequired()]) #一个文本字段
#     submit = SubmitField('Submit')#一个提交按钮
# r'''
#     WTForms支持的HTML标准字段
#     StringField  文本字段
#     TextAreaField  多行文本字段
#     PasswordField   密码文本字段
#     HiddenField 隐藏文本字段
#     DateField   文本字段,值为datetime.date格式
#     DateTimeField   文本字段，值为datetime.datetime 格式
#     IntegerField    文本字段,值为正数
#     DecimalField    文本字段,值为decimal.Decimal
#     FloatField      文本字段,值为浮点数
#     BooleanField    复选框,值为True和False
#     RadioField  一组单选框
#     SelectField     下拉列表
#     SelectMultipleFild  下拉列表,可选择多个值
#     FileField   文件上传字段
#     SubmitField 表单提交按钮
#     FormField   把表单作为字段嵌入另一个表单
#     FiledList   一组指定类型的字段
#
# '''
#
# r'''
#     WTFForms 内建的验证函数如下:
#         Email   验证电子邮件地址
#         EqualTo 比较两个字段的值,常用于要求输入两次密码进行确认的情况
#         IPAddress   验证IPv网络地址
#         Length  验证输入字符串的长度
#         NumberRange 验证输入的值在数字范文之内
#         Optional    无输入值时跳过其他验证函数
#         Required    确保字段中有数据
#         Regexp  使用正则表达式验证输入值
#         URL 验证URL
#         AnyOf   确保输入值在可选值列表中
#         NoneOf  确保输入值不在可选列表中
# '''

r'''
    表单
'''
# from flask import  Flask,render_template,request,Response,session,redirect,url_for,flash
# from flask_wtf import Form
# from wtforms import StringField,SubmitField,PasswordField
# from wtforms.validators import  DataRequired,length
#
# app = Flask(__name__)
# app.config['SECRET_KEY']=('!@#)(*_+)F12quweb@#~ZZ.1BNVC!!!wttx33271944bbhhnPOIUmnhg...!@#')
#
# class LoginForm(Form):
#     loginName = StringField('登录名：',validators=[DataRequired(message='密码不可为空')])
#     loginPass = PasswordField('密&nbsp;&nbsp;&nbsp;&nbsp;码：',validators=[length(6,message='密码长度太短'),DataRequired(message='密码不可为空')])
#     submit = SubmitField('登陆')
# @app.route('/',methods=['POST','GET'])
# def Login():
#     loForm = LoginForm(request.form)
#     userName = None
#     uPass=None
#     if loForm.data['submit']:
#         userName = loForm.loginName.data
#         userPass = loForm.loginPass.data
#         uPass = userPass
#         #session 用于记录对应的数据
#         session['name']=userName
#         session['pass'] = uPass
#         loForm.loginPass.data=''
#         loForm.loginName.data=''
#         flash('Login Success!!!!') #Flash消息 falsh 把消息放入会话中,但是该函数却不能把消息显示出来，我们需要使用Flash把get_flash_message()函数开放给模板，用来获取和渲染模板。
#         return redirect(url_for('Login')) #Http 重定向,redirect函数的参数是重定向的URL,这里使用的重定向URL是程序的根地址,因此重定向的响应体可以写的更简单,写成redirect('/'),url_for函数的第一个且唯一必须指定的参数是端点名，既路由内部的名字。默认情况下，路由的端点是相应的视图函数的名字。
#     return render_template('index.html',loginForm =loForm,userName=session.get('name'))

r'''
    使用数据库:
        可以使用Flask-SQLAlchemy管理数据库：
            安装：pip install Flask-sqlalchemy
        在Flask-sqlalchemy中,数据库使用URL指定
        MySQL   mysql://username:password@hostname/database
        其它数据库类似
        
        在URL中,hostname表示MySQL服务所在的主机,可以是本地主机(localhost)也可以是远程主机。数据库服务器上可能托管多个数据库,因为database表示要使用的数据库名。
        程序使用的数据库URL必须保存到Flask配置对象的SQLALCHEMY_DATABASE_URI键中。
        SQLALCHEMY_ECHO 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
        SQLALCHEMY_POOL_SIZE    数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
        SQLALCHEMY_POOL_TIMEOUT     指定数据库连接池的超时时间。默认是 10。
        SQLALCHEMY_MAX_OVERFLOW     控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃
                
        
'''
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost/mydb'
app.config['SQLALCHEMY_COMMIT_ON_THARDOWN']=True
db = SQLAlchemy(app)

class userTypes(db.Model):
    __tablename__='usertypes'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    typesName=db.Column(db.String(50),unique=True)
    users = db.relationship('Users',backref='userTypes')
class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userName = db.Column(db.String(50),unique=True)
    userTypes_Id = db.Column(db.Integer,db.ForeignKey(userTypes.id))
    def __repr__(self):
        return '<users %s>'%(self.userName)

#
if __name__ == '__main__':
    db.create_all()
    #添加数据
    # usertyp2 = userTypes(typesName='ChuJi')
    # usertyp3 = userTypes(typesName='ZhongJi')
    # usertyp = userTypes(typesName='GaoJi')
    # user = Users(userName='hd',userTypes=usertyp)
    # user1 = Users(userName='hd1',userTypes=usertyp)
    # user2 = Users(userName='hd2',userTypes=usertyp)
    # user3 = Users(userName='hd3',userTypes=usertyp2)
    # user4 = Users(userName='hd4',userTypes=usertyp3)
    # db.session.add(usertyp)
    # db.session.add(usertyp2)
    # db.session.add(usertyp3)
    # db.session.add(user)
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(user3)
    # db.session.add(user4)
    #查询数据
    #Flask-SQLALchemy为每个模型类都提供了query对象。最基本的模型查询 是取回对应表中所有的记录,如下所示
    userTypes = userTypes.query.all()
    for item in userTypes:
        print(item.typesName)
    print('\n\n\n\n\n\n')
    #可以使用过滤器配置query对象进行更精准的数据库查询,如下所示:
    users = Users.query.filter_by(userTypes = userTypes[1]).all()
    for item in users:
        print(item.userName)
        r'''
            查询数据:
                filter()    把过滤器添加到原查询上,返回一个新查询
                filter_by() 把等值过滤器添加到原查询上,返回一个新查询
                limit()     使用指定的值限制原查询返回的结果数量,翻译一个新查询
                offset()    偏移原查询返回的结果,返回一个新查询
                oder_by()   根据指定条件对原查询结果进行排序,返回一个新查询
                group_by()  根据指定条件对原查询结果进行分组,返回一个新查询
                
                例:
                    user = self.db.query(User).filter(User.age==12).offset(2).limit(10).all()  #使用 offset 和limit 配合进行分页
                
            在查询上应用指定的过滤器后,通过调用all()执行查询,以列表的形式返回结果。除了all()之外，还可以使用下面的方法出发查询执行。
            
            常使用的SQLAlchemy查询执行函数:
                all()   以列表形式返回查询的所有结果
                first() 返回查询的第一个结果，如果没有结果,则返回None
                first)or_404()  返回查询的第一个结果,如果没有结果,则终止请求,返回404错误响应
                get()   返回指定主键对应的行,如果没有对应的行,则返回None
                get_or_404()    返回指定主键对应的行,如果没找到制定的主键,则终止请求,返回404错误响应
                count() 返回查询结果的数量
                paginate()  返回一个paginate对象,它包含指定范围内的结果。
            
            from sqlalchemy import func, or_, not_


user = User(name='a')
session.add(user)
user = User(name='b')
session.add(user)
user = User(name='a')
session.add(user)
user = User()
session.add(user)
session.commit()

query = session.query(User)
print query # 显示SQL 语句
print query.statement # 同上
for user in query: # 遍历时查询
    print user.name
print query.all() # 返回的是一个类似列表的对象
print query.first().name # 记录不存在时，first() 会返回 None
# print query.one().name # 不存在，或有多行记录时会抛出异常
print query.filter(User.id == 2).first().name
print query.get(2).name # 以主键获取，等效于上句
print query.filter('id = 2').first().name # 支持字符串

query2 = session.query(User.name)
print query2.all() # 每行是个元组
print query2.limit(1).all() # 最多返回 1 条记录
print query2.offset(1).all() # 从第 2 条记录开始返回
print query2.order_by(User.name).all()
print query2.order_by('name').all()
print query2.order_by(User.name.desc()).all()
print query2.order_by('name desc').all()
print session.query(User.id).order_by(User.name.desc(), User.id).all()

print query2.filter(User.id == 1).scalar() # 如果有记录，返回第一条记录的第一个元素
print session.query('id').select_from(User).filter('id = 1').scalar()
print query2.filter(User.id > 1, User.name != 'a').scalar() # and
query3 = query2.filter(User.id > 1) # 多次拼接的 filter 也是 and
query3 = query3.filter(User.name != 'a')
print query3.scalar()
print query2.filter(or_(User.id == 1, User.id == 2)).all() # or
print query2.filter(User.id.in_((1, 2))).all() # in

query4 = session.query(User.id)
print query4.filter(User.name == None).scalar()
print query4.filter('name is null').scalar()
print query4.filter(not_(User.name == None)).all() # not
print query4.filter(User.name != None).all()

print query4.count()
print session.query(func.count('*')).select_from(User).scalar()
print session.query(func.count('1')).select_from(User).scalar()
print session.query(func.count(User.id)).scalar()
print session.query(func.count('*')).filter(User.id > 0).scalar() # filter() 中包含 User，因此不需要指定表
print session.query(func.count('*')).filter(User.name == 'a').limit(1).scalar() == 1 # 可以用 limit() 限制 count() 的返回数
print session.query(func.sum(User.id)).scalar()
print session.query(func.now()).scalar() # func 后可以跟任意函数名，只要该数据库支持
print session.query(func.current_timestamp()).scalar()
print session.query(func.md5(User.name)).filter(User.id == 1).scalar()

query.filter(User.id == 1).update({User.name: 'c'})
user = query.get(1)
print user.name

user.name = 'd'
session.flush() # 写数据库，但并不提交
print query.get(1).name

session.delete(user)
session.flush()
print query.get(1)

session.rollback()
print query.get(1).name
query.filter(User.id == 1).delete()
session.commit()
print query.get(1)

        '''

    # db.session.commit()
































