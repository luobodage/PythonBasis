"""
author: luoboovo
contact: fuyu16032001@gmail.com
datetime:2021/1/15 12:53
software: PyCharm
        =    =     =
         =   =   =
          =  =  =
        ===========
        =   萝    =
        =   卜    =
        =   神    =
        =   保    =
        =   佑    =
        =   永    =
        =   无    =
        =   bug  =
         =      =
          =    =
             =

"""


# 1.编写出一个通用的人员类（Person），该类具有姓名（Name）、
# 年龄（Age）、性别（Sex）等域。然后对Person 类的继承得到
# 一个学生类（Student），该类能够存放学生的5门课的成绩，并能
# 求出平均成绩。最后在测试函数中对student类的功能进行验证。

class Person:

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex


class Strdent(Person):

    def __init__(self, name, age, sex, *args):
        super().__init__(name, age, sex)
        self.score = args

    def calculateGradePointAverage(self):
        print(f'平均分为:{sum(self.score) / len(self.score)}')


student = Strdent('小明', 18, '男', 80, 90, 100, 200, 400)
student.calculateGradePointAverage()

# 2. 创建一程序，该程序包括一个筛子类，
#  后者有三个数据成员，即筛子的面数，
#  筛子的点数以及包含随机数类的数据成员。
#  为这个类声明一个名为roll（）的成员方法
#  ，它以随机的方式返回下一次掷筛子得的点数。
import random


class sieve:
    def __init__(self, frequency) -> None:
        self.frequency = frequency

    def roll(self):
        while self.frequency > 0:
            print(f'你投的数字为:{random.randint(1, 6)}')
            self.frequency -= 1


s = sieve(frequency=10)
s.roll()

# 3..设计一个BankAccount类，
# 实现银行某账号的资金往来账目管理，
# 包括建账号、存入、取出等。BankAccount类包括，
# 账号（BankAccountId）、开户日期Date(日期)，
# Rest(余额)。另有一个构造函数和三个成员函数
# Bankin()(处理存入账)，Bankout()处理取出账)
# 和和一个负责生成账号的自动增长的函数。

import datetime


class BankAccount:

    def __init__(self, bank_accountId, date, rest) -> None:
        self.bank_accountId = bank_accountId
        self.date = date
        self.rest = rest

    def bankin(self, money):
        self.rest += money
        print(f'存入{money}')

    def bankout(self, money):
        self.rest -= money
        print(f'取出{money}')

    def automaticGrowth(self):
        for i in range(int(datetime.date.today().year) - int(self.date)):
            self.rest = self.rest * (1 + 0.02)
        print(f"您现在的余额是{self.rest}")


bank_name = BankAccount('123', 2010, 100000)
bank_name.bankin(50000)
bank_name.bankout(10000)
bank_name.automaticGrowth()


# 5、 编写一个程序，已有若干学生数据，
# 包括学号、姓名、成绩，要求输出这些学生数据并计算平均分。
# 思路：
#     设计一个学生类Stud,
#     除了包括no(学号)、name(姓名)、和deg(成绩)
#     数据成员外。有两个变量sum和num，分别存放总分和人数，
#     另有一个构造函数、一个普通成员函数disp()和一个成员函数
#     avg()，它用于计算平均分。
class Stud:
    def __init__(self, no, name, deg, __num__, __sum__) -> None:
        self.no = no
        self.name = name
        self.deg = deg
        self.__num__ = __num__
        self.__sum__ = __sum__

    def disp(self):
        print(f'学号:{self.no}\n名字:{self.name}\n成绩:{self.deg}')

    def avg(self):
        print(f'平均分为:{self.__sum__ / self.__num__}')


a = Stud(1, 1, 10, 1, 100)
b = Stud(1, 1, 10, 2, 200)
a.disp()
a.avg()
b.avg()

# 6．设计一个词典类Dic，每个单词包括英文单词及对应的中文含义，并有一个英汉翻译成员函数，通过查词典的方式将一段英语翻译成对应的汉语。
# 思路：    字典项类DicItem包括EngLish(英语单词)、Chinese(对应中文含义)数据成员，字典类包括一个字典项类的列表，包含Add()(添加单词)和trans(英汉翻译)成员函数。
#
# 7.自已封装一个动态元组类，可以根据用户传递的数据，动态的对数组的长度进行扩展；
# 	类名是:MyArray
# 		方法有：
# 			void add(int value);  //追加一个值
# 			vold remove(int index);   //根据索引，删除一个值
# 			void add(int position,int value); //在指定位置插入一个数值
# 			void set(int position,int value); //修改某个位置的数值
# 			int get(int index); //根据索引，获得元数的值
# 			int size();  //获得动态数组中元素的个数；
