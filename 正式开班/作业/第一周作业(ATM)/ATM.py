"""
:author luoboovo
:time 2021/1/8
:realizeFunction ATM简单实现
"""
import csv
import pandas as pd
import pymongo

# 从mongodb数据库获取数据
c = pymongo.MongoClient().get_database("ATM").get_collection('userInfo')


# 获取数据并且生成csv文件 因为这个系统之前是用csv文件写的 所以说这里主要目的是兼容下面的代码
def getDataFromTheDatabase():
    """
    从数据库获取数据并且生成csv文件
    :return:
    """
    # 获取数据库数据
    gen = c.find()
    # 把数据变成DataFrame格式
    data = pd.DataFrame(list(gen))
    # 把数据写成csv格式 pandas自带方法to_csv
    data.to_csv('userInfo2.csv', index=None)


# 用户登录
def logIn():
    """
    用户输入username以及密码 进行验证 读取csv文件 并且如果输入三次错误将冻结
    :return:打印输出
    """
    # 旗标法 判断用户名密码是否匹配
    flag = False
    # 计数
    count = 0
    # 如果输入操作三次
    while count < 3:
        # 定义全局变量
        global username
        # 输入用户名
        username = input("请输入用户名:")
        # print([i for i in userInfo[userInfo.username == username]['password']])
        # 如果用户名在数据文件里
        if username in list(userInfo['username']):
            # 判断用户是否冻结 也就是accountStatus参数是否为0
            if str(userInfo.loc[userInfo['username'] == username, 'accountStatus']) == '0':
                print('您的账户已经冻结,请找银行管理员进行解冻...')
                break
        else:
            print('暂时还没有您的用户名,请联系工作人员进行开户~')
            break
        # 输入密码
        password = input("请输入账户密码:")
        # 验证密码
        for i in userInfo['username']:
            if str([i for i in userInfo[userInfo.username == username]['password']][0]) == password:
                # 如果密码验证成功 返回True
                flag = True
            # 跳出循环
            break
        if flag:
            print('登陆成功~')
            # 打印输出登陆页面
            systemInterface()
            break
        else:
            if count < 2:
                print(f'账户密码错误,您已经试验{count + 1}次,第三次将冻结账户，请谨慎输入...')
            elif count == 2:
                userInfo.loc[userInfo['username'] == username, 'accountStatus'] = 0
                writeFile(fileDirectory)
                print('您的账户已经冻结,请找银行管理员进行解冻...')
        count += 1


# 将文件写入mongodb数据库
def writeFile(filepath):
    """
    :param filepath:传入文件路径
    :return: 生成一个文件 更新文件
    """
    # 先生成新的csv文件
    userInfo.to_csv(filepath, index=False, sep=',')
    # 写入前首先清楚数据库内容 不然会重复写入
    c.delete_many({})
    with open('userInfo2.csv', 'r', encoding='utf-8')as isfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader = csv.DictReader(isfile)
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            each['username'] = str(each['username'])
            each['password'] = str(each['password'])
            each['bankCardNumber'] = str(each['bankCardNumber'])
            each['bankName'] = str(each['bankName'])
            each['accountStatus'] = str(each['accountStatus'])
            each['accountBalance'] = float(each['accountBalance'])
            c.insert(each)


# 查询用户余额
def checkBalances(username):
    """

    :param username:传入参是用户名
    :return:  返回值是用户余额
    """
    # 打印输出用户余额
    # 遍历userInfo的username 当 username=username时 输出accountBalance
    print(f"您的用户余额为:{str([i for i in userInfo[userInfo.username == username]['accountBalance']][0])}")


# 存入金额
def saveMoney(username, money):
    """
    :param username:用户名
    :param money: 要存的金额
    :return: 更新csv文件
    """
    # 判断是否为100的倍数
    if money % 100 == 0:
        # 加钱
        userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
            userInfo.loc[userInfo['username'] == username, 'accountBalance']) + money
        # 重新写入文件 (更新文件)
        writeFile(fileDirectory)
    else:
        print('只能存100或者100元的倍数哦')


# 取钱
def withdrawMoney(username, money):
    """
    :param username:用户名
    :param money: 取得钱
    :return: 更新csv文件
    """
    if money % 100 == 0:
        if money <= int(userInfo.loc[userInfo['username'] == username, 'accountBalance']):
            userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
                userInfo.loc[userInfo['username'] == username, 'accountBalance']) - money
            writeFile(fileDirectory)
        else:
            print('你没有那么多钱啦~')
            checkBalances(username)
    else:
        print('只能取100或者100元的倍数哦')


# 扣除手续费
def deductionFee(username, money):
    """
    :param username:用户名
    :param money: 扣除的手续费
    :return: 更新csv文件
    """
    # 判断钱数够不够扣除手续费
    if money <= int(userInfo.loc[userInfo['username'] == username, 'accountBalance']):
        userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
            userInfo.loc[userInfo['username'] == username, 'accountBalance']) - money
        writeFile(fileDirectory)
    else:
        print('你没有那么多钱啦~')
        checkBalances(username)

# 转账
def transfer(transfer_username, money):
    """
    :param transfer_username:要转账的人的姓名
    :param money: 转账金额
    :return: 更新csv文件
    """
    # 判断是否跨行
    if str([i for i in userInfo[userInfo.username == username]['bankName']][0]) == str(
            [i for i in userInfo[userInfo.username == transfer_username]['bankName']][0]):
        withdrawMoney(username, money)
        saveMoney(transfer_username, money)
    else:
        judge = input('因为是跨行转账要付0.2%的手续费是否继续(y?n):')
        if judge == 'y':
            # 先扣钱
            withdrawMoney(username, money)
            # 然后给对方存钱
            saveMoney(transfer_username, money)
            # 然后扣手续费
            deductionFee(username, money * 0.002)
            print('转账成功')
        else:
            print('取消转账...')


def systemInterface():
    """
    系统界面
    :return:返回一个系统界面
    """
    print('------------------欢迎使用ATM机------------------')
    print('                 输入1-查询余额                 ')
    print('                 输入2-存钱                    ')
    print('                 输入3-取钱                    ')
    print('                 输入4-转账                    ')
    print('                 输入0-退出ATM机               ')
    print('------------------------------------------------')

    flag_1 = True
    while flag_1:
        functionButtons = input('请输入您要使用的功能:')
        if functionButtons.isdigit():
            int_functionButtons = int(functionButtons)
            if 5 >= int_functionButtons >= 0:
                if int_functionButtons == 0:
                    # flag_1 = False
                    break
                    print('谢谢您的使用~祝您生活愉快~')
                elif int_functionButtons == 1:
                    checkBalances(username)
                    systemInterface()
                elif int_functionButtons == 2:
                    money = int(input('请输入你存的金额:'))
                    saveMoney(username, money)
                    checkBalances(username)
                    systemInterface()
                elif int_functionButtons == 3:
                    money = int(input('请输入你取的金额:'))
                    withdrawMoney(username, money)
                    checkBalances(username)
                    systemInterface()
                elif int_functionButtons == 4:
                    transfer_username = input('请输入您要转账的姓名:')
                    money = int(input('请输入您要转账的金额:'))
                    transfer(transfer_username, money)
                    systemInterface()
            else:
                print('请输入0~5的数字哦~')
        else:
            print('请输入正确字符~')


if __name__ == '__main__':
    getDataFromTheDatabase()
    fileDirectory = 'userInfo2.csv'
    userInfo = pd.read_csv(fileDirectory)
    logIn()
