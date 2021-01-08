"""
:author luoboovo
:time 2021/1/8
:realizeFunction ATM简单实现
"""
import pandas as pd

# 获取数据库数据
fileDirectory = 'test.csv'
userInfo = pd.read_csv(fileDirectory)


def logIn():
    """
    用户输入username以及密码 进行验证 读取csv文件 并且如果输入三次错误将冻结
    :return:打印输出
    """
    flag = False
    count = 0
    while count < 3:
        global username
        username = input("请输入用户名:")
        if int(userInfo.loc[userInfo['username'] == username, 'accountStatus']) == 0:
            print('您的账户已经冻结,请找银行管理员进行解冻...')
            break
        password = input("请输入账户密码:")

        for i in userInfo['username']:
            if str([i for i in userInfo[userInfo.username == i]['password']][0]) == password:
                flag = True
            break
        if flag:
            print('登陆成功~')
            systemInterface()
            break
        else:
            if count < 2:
                print(f'账户密码错误,您已经试验{count + 1}次,第三次将冻结账户，请谨慎输入...')
            elif count == 2:
                userInfo.loc[userInfo['username'] == username, 'accountStatus'] = 0
                # userInfo.to_csv("userInfo.csv", index=False, sep=',')
                writeFile(fileDirectory)
                print('您的账户已经冻结,请找银行管理员进行解冻...')

        count += 1


def writeFile(filepath):
    """

    :param filepath:传入文件路径
    :return: 生成一个文件 更新文件
    """
    userInfo.to_csv(filepath, index=False, sep=',')


def checkBalances(username):
    """

    :param username:传入参是用户名
    :return:  返回值是用户余额
    """
    print(f"您的用户余额为:{str([i for i in userInfo[userInfo.username == username]['accountBalance']][0])}")


def saveMoney(username, money):
    """
    :param username:用户名
    :param money: 要存的金额
    :return: 更新csv文件
    """
    if money % 100 == 0:
        userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
            userInfo.loc[userInfo['username'] == username, 'accountBalance']) + money
        writeFile(fileDirectory)
    else:
        print('只能存100或者100元的倍数哦')


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


def deductionFee(username, money):
    """
    :param username:用户名
    :param money: 扣除的手续费
    :return: 更新csv文件
    """
    if money <= int(userInfo.loc[userInfo['username'] == username, 'accountBalance']):
        userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
            userInfo.loc[userInfo['username'] == username, 'accountBalance']) - money
        writeFile(fileDirectory)
    else:
        print('你没有那么多钱啦~')
        checkBalances(username)


def transfer(transfer_username, money):
    """
    :param transfer_username:要转账的人的姓名
    :param money: 转账金额
    :return: 更新csv文件
    """
    if str([i for i in userInfo[userInfo.username == username]['bankName']][0]) == str(
            [i for i in userInfo[userInfo.username == transfer_username]['bankName']][0]):
        withdrawMoney(username, money)
        saveMoney(transfer_username, money)
    else:
        judge = input('因为是跨行转账要付0.2%的手续费是否继续(y?n):')
        if judge == 'y':
            withdrawMoney(username, money)
            saveMoney(transfer_username, money)
            deductionFee(username, money * 0.002)
            print('转账成功')
            checkBalances()
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
    print('-----------------------------------------------')
    functionButtons = input('请输入您要使用的功能:')

    while True:
        if functionButtons.isdigit():
            int_functionButtons = int(functionButtons)
            if 5 >= int_functionButtons >= 0:
                if int_functionButtons == 0:
                    print('谢谢您的使用~祝您生活愉快~')
                    break
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
    logIn()
