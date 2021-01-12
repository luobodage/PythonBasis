# 登录验证前  把登录信息存入日志文件 excel   日志信息：当前系统时间，用户名，密码
# 登陆后，不管成功还是失败  也要将日志信息存入日志文件  日志信息：当前系统时间，用户名，密码 ,是否登录成功
import datetime


def outter(args):
    def inner(username, password):
        global val
        val = input("请输入验证密码:")
        if val == '1111':
            print("验证码正确")
            args(username, password)
            write_log()
        else:
            print('验证码错误')
            write_log()

    return inner


def preparecsv():
    with open('log.csv', 'w') as f:
        f.write('时间,验证码,是否成功,用户名,密码\n')


def write_log():
    flag = False
    with open('log.csv', 'a') as f:
        if val == '1111' and username == '1' and password == '2':
            flag = True
        f.write(f'{datetime.datetime.now()},{val},{flag},{username},{password}\n')


@outter
def login(username, password):
    if username == '1' and password == '2':
        print('登陆成功')
    else:
        print('登陆失败')


if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')
    # preparecsv()
    login(username, password)

# print(f"{datetime.datetime.hour} : {datetime.datetime.minute}")
