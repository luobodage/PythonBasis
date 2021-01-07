# 1
# 盈盈为了考验令狐冲夺冠的决心，要他说一百遍“我能行！”
#

print("-----------------------------------")
print("盈盈为了考验令狐冲夺冠的决心，要他说一百遍“我能行！”")
for i in range(100):
    print("我能行！")

# 2.
# 本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年内，每年获得的本金是多少？
print("-----------------------------------")
print("本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年内，每年获得的本金是多少？")
principal = 10000
for i in range(1, 6):
    principal += principal * 0.0003
    print(f"第{i}年有{principal}元")

# 3.
# 计算出1—100
# 之间所有能被3整除的整数的和？
#

print("-----------------------------------")
print("""计算出1—100
# 之间所有能被3整除的整数的和？""")
sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum += i
print(sum)

# 4.
# 计算1000以内所有不能被7整除的整数之和？
#
print("-----------------------------------")
print("计算1000以内所有不能被7整除的整数之和？")
sum = 0
for i in range(1, 1001):
    if i % 7 != 0:
        sum += i
print(sum)

# 5.
# 用while做
# 求10到20的累加和
#
print("-----------------------------------")
print("""
用while做
求10到20的累加和
""")
sum = 0
i = 10
while 10 <= i <= 20:
    sum += i
    i += 1
print(sum)
# 6.
# 找出一个数的所有因子数
#
print("-----------------------------------")
print("找出一个数的所有因子数")
number = int(input("请输入一个数:"))
for i in range(1, number // 2 + 1):
    if number % i == 0:
        print(f"{i}是{number}的因子数")
    else:
        print("这个数字没有因子数")
# 7.
# 输入一个数，判断这个数是否是素数；
print("-----------------------------------")
print("输入一个数，判断这个数是否是素数；")
number = int(input("请输入一个数:"))
flag = False
for i in range(1, number // 2 + 1):
    if number % i == 0:
        flag = True
if not flag:
    print("这个数不是素数")
#
#
# 8
# 定义一个正整数如：1205
# 统计它的各位数字中零的个数，并求各位数字中的最大者。
#
print("-----------------------------------")
print("""
定义一个正整数如：1205
统计它的各位数字中零的个数，并求各位数字中的最大者。
""")
number = input("请输入一个数,我会计算其中的零的个数:")
count = 0
if len(number) > 1:
    number_list = list(number)
    for i in number_list:
        if i == '0':
            count += 1
    print(f"零的个数为{count}")
else:
    print("您输入的数字个数太短")
print(f"这个数面最大的是{max(number)}")
# 9
# 有1020个西瓜，第一天卖掉总数的一半后又多卖出两个，以后每天卖剩下的一半多两个，问几天以后能卖完
#
print("-----------------------------------")
print("有1020个西瓜，第一天卖掉总数的一半后又多卖出两个，以后每天卖剩下的一半多两个，问几天以后能卖完")
total = 1020
count = 0
while total > 0:
    total = total // 2 - 2
    count += 1
print(count)

# 10
# 猴子吃桃问题： 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，第二天早上又将剩下的桃子吃了一半，又多吃一个，以后每天都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子。求第一天共摘了多少个？
#
print("-----------------------------------")
print(
    "猴子吃桃问题： 猴子第一天摘下若干个桃子，当即吃了一半，"
    "还不过瘾，又多吃了一个，第二天早上又将剩下的桃子吃了一半，"
    "又多吃一个，以后每天都吃了前一天剩下的一半零一个。到第10"
    "天早上想再吃时，见只剩下一个桃子。求第一天共摘了多少个？")
day = 10
sum = 1
while day > 1:
    sum = (sum * 2) + 2
    day -= 1
print(sum)
# 11
# 判断一个数是否是完全数（完数指的是一个数的所有因子数的和等于这个数本身，例如
# 6 = 1 + 2 + 3, 即6就是完全数）
#
print("-----------------------------------")
print("""
判断一个数是否是完全数（完数指的是一个数的所有因子数的和等于这个数本身，例如
6 = 1 + 2 + 3, 即6就是完全数）
""")
number = int(input("请输入一个数(用来判断是否是完全数):"))
count = 0
for i in range(number // 2):
    if number % i == 0:
        count += i
if count == number:
    print("为完全数")
else:
    print("不是完全数")

# 12.
# 循环录入某学生5门课的成绩并计算平均分，如果某分数录入为负，停止录入并提示录入错误（使用break）
for i in range(5):
    if i == 0:
        chinesePerformance = int(input("请输入语文成绩:"))
        if chinesePerformance < 0:
            print("输入成绩错误")
    elif i == 1:
        mathPerformance = int(input("请输入数学成绩:"))
        if mathPerformance < 0:
            print("输入成绩错误")
    elif i == 2:
        englishPerformance = int(input("请输入英语成绩:"))
        if englishPerformance < 0:
            print("输入成绩错误")
    elif i == 3:
        physicalPerformance = int(input("请输入物理成绩:"))
        if physicalPerformance < 0:
            print("输入成绩错误")
    elif i == 4:
        chemistryPerformance = int(input("请输入化学成绩:"))
        if chemistryPerformance < 0:
            print("输入成绩错误")

print(
    f"平均成绩为{(chinesePerformance + mathPerformance + englishPerformance + physicalPerformance + chemistryPerformance) / 5}")

# 13.
# 循环录入python课的学生成绩，统计分数大于等于
# 80
# 分的学生比例(使用continue)
count = 0
for i in range(10):
    score = int(input("请输入学生成绩:"))
    if score >= 80:
        count += 1
print(f"最后的比例是{count / 10}")
# 1.
# 输出图型
# *
# **
# ***
# ****
# *****
# ******
#
print("-----------------------------------")
"""
输出图型
*
**
***
****
*****
******
"""
for i in range(6):
    for j in range(i + 1):
        print('*', end='')
    print()

# 2
# 输出图型
# ** ** ** *
# ** ** **
# ** ** *
# ** **
# ** *
# **
# *
print("-----------------------------------")
print("""
输出图型
** ** ** *
** ** **
** ** *
** **
** *
**
*
""")
for i in range(6):
    for j in range(i, 6):
        print('*', end='')
    print()

# 3
# 把12题的两个图型合成一个。
print("-----------------------------------")
print("""
把12题的两个图型合成一个。
""")
for i in range(6):
    for j in range(i + 1):
        print('*', end='')
    print()
    if i == 5:
        for i in range(5):
            for j in range(i, 5):
                print('*', end='')
            print()

# 4.
# 编写一个九九乘法法
print("-----------------------------------")
print("编写一个九九乘法法")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}", end=' ')
    print()

# 5
# 百钱买百鸡，有100元钱，要去买100只鸡，公鸡5元一只，母鸡3元一只，小鸡1元3只，问公，母，小鸡各买多少只。
# 提示： a + b + c = 100
# 只
# 5
# a + 3
# b + 1 / 3
# c = 100
# 钱

print("-----------------------------------")
print("""
百钱买百鸡，有100元钱，要去买100只鸡，公鸡5元一只，母鸡3元一只，小鸡1元3只，问公，母，小鸡各买多少只。
提示： a + b + c = 100只 5a + 3b + 1 / 3c = 100
钱
""")
for a in range(0, 21):
    for b in range(0, 34):
        c = 100 - a + b
        if 5 * a + 3 * b + c / 3 == 100 and a + b + c == 100:
            print(f"公鸡{a}只,母鸡{b}只,小鸡{c}只")

    # 6
# 星型图案
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *

print("-----------------------------------")
print("""
# 星型图案 
*
** *
** ** *
** ** ** *
** ** ** ** *
""")
for i in range(1, 6):
    for j in range(1, 2 * i):
        print('*', end=' ')
    print()

# 7
# 把上图形再倒过来，合成一个菱形图案
print("-----------------------------------")
print("把上图形再倒过来，合成一个菱形图案")
for i in range(1, 6):
    for j in range(1, 2 * i):
        print('*', end='')
    print()
for i in range(1, 6):
    for j in range(1, 2 * i):
        print(' ', end='')
    for k in range(11 - 2 * i, 0, -1):
        print('*', end='')
    print()

# 8
# 打印出一个空菱形图案
print("-----------------------------------")
print("打印出一个空菱形图案")
for i in range(1, 6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(1, 6):
    for j in range(1, 2 * i):
        print(' ', end='')
    for k in range(11 - 2 * i, 0, -1):
        if k == 11 - 2 * i or k == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 9.
# 求300 - 400
# 之间的素数
print("-----------------------------------")
print("""
求300 - 400之间的素数
""")
flag = False
for i in range(300, 401):
    for j in range(1, i // 2 + 1):
        if i % j != 0:
            flag = True
    if flag:
        print(f"{i}不是素数")

# 10
# 输出一个平行四边形的图案
print("-----------------------------------")
print("输出一个平行四边形的图案")
for i in range(1, 6):
    for j in range(1, 2 * i):
        print('*', end='')
    print()
for i in range(1, 6):
    for j in range(1, 2 * i):
        print(' ', end='')
    for k in range(11 - 2 * i, 0, -1):
        print('*', end='')
    print()
# 11
# 用while做
# 鸡兔同笼。鸡兔一共有50只，脚一共有160只，问鸡和兔各多少只?要求鸡兔至少一样一只。
print("-----------------------------------")
print("""
用while做
鸡兔同笼。鸡兔一共有50只，脚一共有160只，问鸡和兔各多少只?要求鸡兔至少一样一只。
""")
for chicken in range(50):
    for rabbit in range(50):
        if chicken + rabbit == 50 and 4 * rabbit + 2 * chicken == 160:
            print(f"鸡有{chicken}只,兔子有{rabbit}只")
# 12.
# 计算2 / 1 + 3 / 2 + 4 / 3 +…+(n + 1) / n，写出算法的程序.
#
print("-----------------------------------")
print("计算2 / 1 + 3 / 2 + 4 / 3 +…+(n + 1) / n，写出算法的程序.")
number = float(input("请输入一个数字:"))
sum = 0
for i in range(1, int(number + 1)):
    sum = sum + (i + 1) / i
print(sum)
# 13.2000
# 年我国人口为13亿，如果人口每年的自然增长率为7 %，那么多少年
# 后我国人口将达到15亿？设计一个算法的程序
#

print("-----------------------------------")
print("""
2000年我国人口为13亿，如果人口每年的自然增长率为7 %，那么多少年后我国人口将达到15亿？设计一个算法的程序
""")
population = 1300000000
count = 0
while population <= 1500000000:
    population += population * 0.07
    count += 1

print(f"要{2000 + count}年 就可以达到15亿了")
# 14.
# 给出50个数，1，2，4，7，11，„，其规律是：第1个数是1，第2个数比第1个数大1，第3个数比第2个数大2，第4个数比第3个数大3，„，以此类推.要求计算这50个数的和.先将下面给出的程序框图，再根据程序框图写出程序.
#
print("-----------------------------------")
print("""
给出50个数，1，2，4，7，11，„，其规律是：第1个数是1
，第2个数比第1个数大1，第3个数比第2个数大2，第4个数比
第3个数大3，„，以此类推.要求计算这50个数的和.
先将下面给出的程序框图，再根据程序框图写出程序.
""")
sum = 1
for i in range(1, 50):
    sum = i  + sum
    print(sum)
# 15
# 有个人想知道，一年之内一对兔子能繁殖多少对？于是就筑了一道围墙把一对兔子
# 关在里面。已知一对兔子每个月可以生一对小兔子，而一对兔子从出生后第3个月起每
# 月生一对小兔子。假如一年内没有发生死亡现象，那么，一对兔子一年内（12
# 个月）能繁殖成多少对？  分析：兔子的规律为数列，1，1，2，3，5，8，13，21
print("-----------------------------------")
print("""
有个人想知道，一年之内一对兔子能繁殖多少对？于是就筑了一道围墙把一对兔子
关在里面。已知一对兔子每个月可以生一对小兔子，而一对兔子从出生后第3个月起每
月生一对小兔子。假如一年内没有发生死亡现象，那么，一对兔子一年内（12
个月）能繁殖成多少对？  分析：兔子的规律为数列，1，1，2，3，5，8，13，21
""")
number = int(input("请输入您要计算的月数(不计算兔子伤亡与死亡):"))
# L = [i for i in range(1, number + 1)]
L = list(range(1, number + 1))
fibonacci = []
for i in range(len(L)):
    if L[i] == 1 or L[i] == 2:
        fibonacci.append(1)
    else:
        j = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(j)
print(f"第{number + 1}个月一共有{fibonacci[-1]}只兔子")

# 16.
# 水仙花数（Narcissistic
# number）也被称为超完全数字不变数、自恋数、自幂数，水仙花数是指一个
# n
# 位数（n≥3 ），它的每个位上的数字的
# n
# 次幂之和等于它本身（例如：1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 153）, 请通过程序找出所有的3位数的水仙花数（穷举法）
for i in range(100, 1000):
    str_i = str(i)
    if int(str_i[0]) ** 3 + int(str_i[1]) ** 3 + int(str_i[2]) ** 3 == i:
        print(f"{i}是水仙花数")

# 17.
# 从控制台输入一个正整数，并进行反转输出
number = input("请输入一个正整数:")
print(number[::-1])
