import requests
import lxml.etree as lx

# 要爬取的网站
url = 'https://www.bilibili.com/'

# get这个网站的网页内容
content = requests.get(
    url=url,
    # 头文件是为了 模仿人类浏览器浏览 (现在大多数i都有反爬虫机制)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
).content

# 把二进制内容转化成xml形式 (可以理解为树的形式 就是一个一个标签 然后通过xpath的方式找到标签的内容)
content_xl = lx.HTML(content)

# 通过xpath 找到封面图片的 url 并且保存
donghua = content_xl.xpath('//*[@id="bili_report_guochuang"]/div[2]/div[1]/div/div[11]/div/a/img/@src')

tupian = requests.get(
    # 要用http协议进行连接 并且访问 因为 xpath返回的数据是列表 所以用索引来定位
    url='http:' + donghua[0]
).content

# 进行保存 以二进制的方式 进行写入
with open('get到啦.jpg', 'wb') as f:
    f.write(tupian)
