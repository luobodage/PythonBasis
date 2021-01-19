# Django初识

#### 安装Django到本机环境

~~~shell
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
~~~

![image-20210119103837893](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119103837893.png)

#### 创建Django项目

~~~shell
django-admin startproject Test(Test为项目名)
~~~

或者利用pycharm创建项目

![image-20210119104015055](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119104015055.png)

ps:virtualenv为虚拟环境，不太了解的可以直接使用自己安装的环境...

#### 切换到项目的根目录，启动项目

~~~shell
cd Test (进入Test根目录 也就是你创建的Test文件)

python manage.py runserver 0.0.0.0:8080

默认端口为8000 浏览器本地访问:127.0.0.1:8080即可看到默认的首页
~~~

![image-20210119104339188](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119104339188.png)

![image-20210119104404949](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119104404949.png)

#### Django数据库

默认项目根目录下自动创建'db.sqlite3'文件 可以在settings.py里面指定'db.sqlite3'文件的存放路径或者更改其他的数据库引擎,如MySQL

![image-20210119104642412](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119104642412.png)

#### 访问Django的admin管理后台

访问路径：127.0.0.1:8000/admin （开始无法访问，因为数据库还未初始化，提示没有这个表）

##### (1).数据库迁移

makemigrations创建数据库迁移，产生SQL脚本，使用migrate命令把默认的model同步到数据库，
Django会自动为model建立数据库表。

###### 数据库迁移

python manage.py makemigrations

![image-20210119105454745](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119105454745.png)

###### 自动生成数据库表

python manage.py migrate
此时访问127.0.0.1:8080/admin即可看到后台登录页面。

![image-20210119105504524](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119105504524.png)

##### (2).创建后台管理员账号

python manage.py createsuperuser 
根据提示输入对应的用户名，邮箱和密码

![image-20210119105519554](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119105519554.png)

进入127.0.0.1:8080/admin

输入刚才设置的账号密码点击login

![image-20210119105912145](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119105912145.png)

就跳转到Django后台啦

![image-20210119105926899](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210119105926899.png)

##### (3).配置文件settings.py解读

调试模式，应用注册，第三方库配置，国际化等