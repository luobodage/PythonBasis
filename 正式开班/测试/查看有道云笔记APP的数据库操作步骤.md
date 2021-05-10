## 查看有道云笔记APP的数据库操作步骤

1、用adb进行连接

2、进入模拟器shell界面

~~~shell
adb shell
~~~

3、界面为这样代表进入成功

![image-20210507093417380](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507093417380.png)

4、进入/data/data目录 此目录是安装的包

5、ls -l 进行查看 可以通过正则查找

![image-20210507093552111](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507093552111.png)

查看到有databases数据库

进入databases数据库文件夹

用pwd查看路径文件

5、ctrl+D退出Android shell模式

6、用adb把数据库文件拉出来

~~~shell
adb pull /data/data/com.youdao.note/databases
~~~

将文件拉到操作系统中 不写默认目录

7、获取到文件

![image-20210507095041122](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507095041122.png)

8、![image-20210507093934589](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507093934589.png)

具体的笔记数据都是在unlogin@unlogin_ynote.db里面

可以选择用pycharm打开或者navicat打开

#### 1-->PyCharm打开

![image-20210507094052834](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507094052834.png)

#### 2-->Navicat打开

(1)建立sqlit3连接

![](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/jianlilianjie.png)

(2)找到unlogin@unlogin_ynote.db文件

![image-20210507094205102](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/image-20210507094205102.png)

(2)查看note_meta数据库

![](https://luoboovovimages.oss-cn-beijing.aliyuncs.com/img/xiaoguozhanshi.png)

