

#### 准备工作

下载 bitnami-lampstack-8.0.3-2-linux-x64-installer.run

工具包：bitnami-wordpress-5.7.1-0-module-linux-x64-installer.run



#### 1.安装lamp

先用工具传入linux下，找到文件路径 ps：我的路径是/root/

首先修改权限

~~~shell
chmod 755 bitnami-lampstack-8.0.3-2-linux-x64-installer.run
~~~

执行bitnami-lampstack-8.0.3-2-linux-x64-installer.run

~~~shell
./bitnami-lampstack-8.0.3-2-linux-x64-installer.run
~~~

一路Y

![image-20210422123710510](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422123710510.png)

跳转出设置文件夹页面

![image-20210422123801796](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422123801796.png)

按回车

设置MySQL的root密码   ps:要记住 后面要用

![image-20210422123835198](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422123835198.png)

后面就一直回车

![image-20210422123910906](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422123910906.png)

等待安装完成

![image-20210422123919421](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422123919421.png)

完成之后通过ip进行访问

![image-20210422124325955](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124325955.png)

出现以上页面为成功 可以进行下一步

#### 2.安装应用（以wordpress个人博客为例）

给权限

~~~shell
chmod 755 bitnami-wordpress-5.7.1-0-module-linux-x64-installer.run
~~~

运行

~~~shel
./bitnami-wordpress-5.7.1-0-module-linux-x64-installer.run 
~~~

![image-20210422124606966](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124606966.png)

选择语言选择中文

![image-20210422124625980](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124625980.png)

文件夹选择到/opt/lampstack-8.0.3-2

![image-20210422124721568](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124721568.png)

![image-20210422124747202](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124747202.png)

用户名密码都填自己的

密码就是上面设置的MySQL密码

![image-20210422124855838](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124855838.png)

配置如下

![image-20210422124931256](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422124931256.png)

等待安装

![image-20210422125013086](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422125013086.png)

查看页面

地址为：http://192.168.101.100/wordpress/   

![image-20210422125122941](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422125122941.png)

进入管理界面

http://192.168.101.100/wordpress/admin

![image-20210422125227257](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210422125227257.png)

用户名为你设置的

密码是mysql的root密码