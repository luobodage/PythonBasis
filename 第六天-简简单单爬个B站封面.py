import requests
import lxml.etree as lx

url = 'https://www.bilibili.com/'

content = requests.get(
    url=url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
).content


content_xl = lx.HTML(content)

print(type(content_xl))

donghua = content_xl.xpath('//*[@id="bili_report_guochuang"]/div[2]/div[1]/div/div[11]/div/a/img/@src')



tupian  = requests.get(
    url = 'http:' + donghua[0]
).content

with open('get到啦.jpg' , 'wb') as f :
    f.write(tupian)

