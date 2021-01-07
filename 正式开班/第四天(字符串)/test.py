# 1.
# 字符串解析, 现有一字符串, "卡巴斯基#杀毒软件#免费版#俄罗斯#", 解析出每个元素。
print("--------------------------------------------")
print("""字符串解析, 现有一字符串, "卡巴斯基#杀毒软件#免费版#俄罗斯#", 解析出每个元素。""")
str_1 = "卡巴斯基#杀毒软件#免费版#俄罗斯#"
for i in str_1.split('#'):
    print(i, end=' ')
# 2.
# "那车水马龙的人世间,那样地来 那样地去,太匆忙"
# 最后一次出现
# "那"
# 的位置。
print("--------------------------------------------")
print("""
"那车水马龙的人世间,那样地来 那样地去,太匆忙"最后一次出现"那"的位置。
""")
print("那车水马龙的人世间,那样地来 那样地去,太匆忙".rfind('那'))

# 3.
# 判断输入的字符串是否是.py结束
# 有一身份证号, 判断此为男还是女, 基于此方法, 写一个算法, 判断一个身份证号为男还是女。（身份证分15位和18位）
print("--------------------------------------------")
print("判断输入的字符串是否是.py结束")
fileName = 'Test.py'
print(fileName.endswith('.py'))
print("有一身份证号, 判断此为男还是女, 基于此方法, 写一个算法, 判断一个身份证号为男还是女。（身份证分15位和18位）")
identityNumber = '身份证号'
print("男" if int(identityNumber[-2]) % 2 != 0 else "女")
# 4.
# 有如下格式的字符串name - age - sex - address, 解析出姓名, 年龄等信息。
print("--------------------------------------------")
str_04 = 'name - age - sex - address'
for i in str_04.split(' - '):
    print(i)

# 5.
# 求出字符串中有多少种字符，以及每个字符的个数
# 例如有字符串
# str = "apple is a apple.";
# 结果应该是
# a: 3
# p: 4
# l: 2
# e: 2
# :3
# i: 1
# s: 1
# .:1
print("--------------------------------------------")
print("""
求出字符串中有多少种字符，以及每个字符的个数
例如有字符串
str = "apple is a apple."
结果应该是
a: 3
p: 4
l: 2
e: 2
:3
i: 1
s: 1
.:1
""")
str_05 = "apple is a apple."
list_str = []

for i in range(len(str_05)):
    list_str.append(f"{str_05[i]}:{str_05.count(str_05[i])}")
set_str = set(list_str)
for i in set_str:
    print(i)

# 6.
# 用来去掉字符串右边的空格
#
str_1.rsplit(' ')

# 7.
# 定义一个方法，将str所指字符串的正序和反序进行连接, 例如
# "ok"->"okko"
#
print("--------------------------------------------")


def reverseConnection(str):
    return str + str[-1::-1]


print(reverseConnection('lala'))
# 8.
# 字符串右移n位, 例如
# "helloworld"
# 右移两位
# 后ldhellowor
#
print("--------------------------------------------")
print("""
字符串右移n位, 例如
"helloworld"
右移两位
后ldhellowor
""")


def stringMovingCombination(str, n):
    print(str[len(str) - n:len(str)] + str[:len(str) - n])


stringMovingCombination("HelloWorld", 3)

# 9.
# 求5个字符串中最长的那个，把最长的字符串打印出来
print("--------------------------------------------")

print("求5个字符串中最长的那个，把最长的字符串打印出来")


def longestString(str1, str2, str3, str4, str5):
    long = max(len(str1), len(str2), len(str3), len(str4), len(str5))
    if long == len(str1):
        print(str1)
    elif long == len(str2):
        print(str2)
    elif long == len(str3):
        print(str3)
    elif long == len(str4):
        print(str4)
    elif long == len(str5):
        print(str5)


longestString('123', '2323', '23123123', 'lalalla', 'woshizuichangde')
# 10.
# 若可以从一个源字符串中， 找到一个相符的字符串(忽略大小写)， 则返回第一个字符的索引位置，否则返回 - 1。
print("--------------------------------------------")
print("若可以从一个源字符串中， 找到一个相符的字符串(忽略大小写)， 则返回第一个字符的索引位置，否则返回 - 1。")
str_10 = 'askjhdkjahsdjka'
print(str_10.upper().find('A'))

# 11.
# 判断一个字符串是否是回文
print("--------------------------------------------")
print("判断一个字符串是否是回文")
str_11 = input("请输入一个字符串:")
flag = False
for i in range(len(str_11) // 2):
    if str_11[i] == str_11[-(i + 1)]:
        flag = True
if flag:
    print("回文")
else:
    print("不回文")

# 12.
# 如下字符串, 01  # 张三#20-02#李四#30-03#王五#40。。。。。。,解析每个人分数多少。样式如下：
# 01
# 张三
# 20
# 02
# 李四
# 30
# 03
# 王五
# 40。并且计算总分。
print("--------------------------------------------")
print("""
如下字符串, 01#张三#20-02#李四#30-03#王五#40。。。。。。,解析每个人分数多少。样式如下：
01
张三
20
02
李四
30
03
王五
40。
并且计算总分
""")
str_12 = '01#张三#20-02#李四#30-03#王五#40'
aPerson = str_12.split('-')
allPeople = []
sum_1 = 0
count = 0
for i in aPerson:
    allPeople.append(i.split('#'))
for i in allPeople:
    for j in i:
        print(j)
    sum_1 += int(i[2])
    count += 1
print(f"平均成绩为{sum_1 / count}")
# 编程.
# 1.
# 已知字符串："this is a test of python".
# 按要求执行以下操作：
# (1)
# 统计该字符串中字母s出现的次数
# (2)
# 取出子字符串
# "test"
# (3)
# 将字符串中每个单词的第一个字母变成大写， 输出到控制台。
# (4)
# 用两种方式实现该字符串的倒叙输出。
print("--------------------------------------------")
print("""
已知字符串："this is a test of python".
按要求执行以下操作：
(1)统计该字符串中字母s出现的次数
(2)取出子字符串"test"
(3)将字符串中每个单词的第一个字母变成大写， 输出到控制台。
(4)用两种方式实现该字符串的倒叙输出。
""")
str_01 = "this is a test of python"
print("(1)统计该字符串中字母s出现的次数")
print(str_01.count('s'))
print("""(2)取出子字符串"test".""")
print(str_01[10:14])
print("(3)将字符串中每个单词的第一个字母变成大写， 输出到控制台。")
print(str_01.title())
print("(4)用两种方式实现该字符串的倒叙输出。")
print(str_01[-1::-1])
for i in range(len(str_01)):
    print(str_01[-(i + 1)], end='')
#
# 2.
# 获取一个字符串在另一个字符串中出现的次数
# 例如, 获取
# "kk"
# 在
# "abkkcdkkefkkskk"
# 中出现的次数
#
print("--------------------------------------------")
print("""
获取一个字符串在另一个字符串中出现的次数例如, 获取"kk"在"abkkcdkkefkkskk"中出现的次数
""")
str_02 = 'abkkcdkkefkkskk'
print(str_02.count('kk'))

# 3.
# 去除字符串两端的逗号
print("--------------------------------------------")
print("去除字符串两端的逗号")
str_03 = ',,,,,123,,,,,'
print(str_03.strip(','))

# 4.
# 将一个字符串进行反转
# 将字符串中指定部分进行反转，"abcdefgeee";
print("--------------------------------------------")
print("""
将一个字符串进行反转
将字符串中指定部分进行反转，"abcdefgeee";
""")
str_04 = 'abcdefgeee'


def specifyCharacterReverse(str, sub):
    position = str.find(sub)
    print(str[position:] + str[:position])


specifyCharacterReverse(str_04, 'e')
# 5.
# 获取两个字符串中最大相同子串
# 例如找到字符串
# "abcwerthelloyuiodef"
# 和
# "cvhellobnm"
# 中的最大相同字串
#
# 此题，应该从子串的长度考虑。
# 思路：
# 1，将短的那个子串按照长度递减的方式获取到。
# 2，将每获取到的子串去长串中判断是否包含，如果包含，已经找到！。
str_one = 'ashdhhhqii'
str_two = 'ashkjasjkhjkashdhsa'
number_max = 0
count = ''
for i in range(len(str_one)):
    for j in range(len(str_two)):
        if str_one[i] == str_two[j] and (str_one[i] not in count):
            count = count + str_one[i]
            number_max = len(count)
            break
if len(count) > number_max:
    number_max = len(count)
print(number_max)
print(count)

# 6.
# 给你一组字符串如：iu7i8hy4jnb2，让你编程输出里面的数字：
#
print("--------------------------------------------")
print("给你一组字符串如：iu7i8hy4jnb2，让你编程输出里面的数字：")
str_06 = 'iu7i8hy4jnb2'
for i in list(str_06):
    if i.isdigit():
        print(i, end=' ')

# 7.
# 假设字符串类似这样的aba和aab就相等，现在随便给你二组字符串，请编程比较他们看是否相等
#
print("--------------------------------------------")
print("假设字符串类似这样的aba和aab就相等，现在随便给你二组字符串，请编程比较他们看是否相等")


def determineWhetherTheyAreEqual(a, b):
    a_set = set(list(a))
    b_set = set(list(b))
    if len(a) == len(b) and a_set == b_set:
        print("你们相等")
    else:
        print("你们不相等")


determineWhetherTheyAreEqual('ababcae', 'caebbaa')
