import requests
import lxml.etree as le
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Cookie': 'ZHID=C8EEEFF1E968B289839A10BAD562321E; ver=2018; zhffr=www.baidu.com; v_user=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTmin1Q4RALsjNX47iDG11ebI9VH2akUxv3br-oIIZViPLWOicQ4wtBIjU5flKQsv%26wd%3D%26eqid%3Df496571b000a48ca000000035fe43cd7%7Chttp%3A%2F%2Fwww.zongheng.com%2F%7C27028512; JSESSIONID=abca5p1EPEmTBaeqEJtAx; rSet=1_3_1_14'
}


def get_url():
    home_url = 'http://book.zongheng.com/showchapter/672340.html'

    content = requests.get(
        url=home_url,
        headers=headers
    ).content

    content_lxml = le.HTML(content)
    global content_p

    content_p = content_lxml.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/ul/li/a/@href')
    for i in content_p:
        print(i)


def get_content():
    for i in range(len(content_p)):
        with open(f'小说文件/第{i + 1}章.txt', 'w', encoding='utf-8') as f:
            content = requests.get(
                url=content_p[i],
                headers=headers,
            ).content
            content_lxml = le.HTML(content)
            content_pp = content_lxml.xpath('//*[@id="readerFt"]/div/div[5]/p/text()')
            for j in content_pp:
                f.write(j)
                f.write('\n')


if __name__ == '__main__':
    get_url()
    get_content()