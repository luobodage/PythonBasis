import helium
# 比较适合新手的自动化库
from time import sleep

home_url = 'https://mail.163.com/'  # 网站主地址
user_name = 'luobomc'  # 登陆用户名
password = '*'  # 密码

driver = helium.start_chrome(home_url)  # 打开浏览器 并且打开home_url地址页面
sleep(5)  # 睡眠5s等待页面加载
helium.write(user_name, helium.TextField('邮箱帐号或手机号码'))  # 锁定'邮箱账号或手机号码'并且锁定 然后传入用户名
sleep(2)  # 睡眠2秒
helium.write(password, helium.TextField('输入密码'))  # 锁定密码输入框并且输入
helium.press(helium.ENTER)  # 模拟按回车 登录
sleep(5)  # 睡眠5秒等待页面刷新
helium.click(helium.Text('收 信'))  # 点击收信按钮 查看邮件
helium.kill_browser()  # 关闭浏览器
