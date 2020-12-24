import requests as rq
from 第七天 import GetCookie


def spdier():
    # 这里传入的是页数以及输入的关键字
    cookie = GetCookie.get_cookie(2, 'java')
    # 从拉勾网找到数据的url 可以通过ctrl+f 的方法 千万不要用眼睛找
    home_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=true'
    headers = {
        # 模拟android登录网页
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 网站的根
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        # 返回推荐的网站
        'Referer': 'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true',
        # 网站的语言格式
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        # android的cookie 以后可以写一个获取cookie的方法进行实时动态获取
        # 'Cookie': 'JSESSIONID=ABAAAECABFAACEA5494E1678FB5942947BF90F6A9FD61CC; WEBTJ-ID=20201224091240-176924e18a2d32-0f0f4d96c8edcc-c791039-2073600-176924e18a3c21; RECOMMEND_TIP=true; user_trace_token=20201224091242-67dc32a1-823d-425d-a6de-480d2a1486bc; LGSID=20201224091242-2f43d2b3-c244-4a70-874a-2f20804dcb20; LGUID=20201224091242-cf35be41-4df6-427f-8373-c7c52d4c4a13; _ga=GA1.2.159587496.1608772362; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; _gat=1; X_HTTP_TOKEN=4a7ea378b9f1662b8954778061c3d157319b2da989; LGRID=20201224094959-c660ad90-9639-4c9a-a04c-bf07fa6bc8e9; SEARCH_ID=568d053fd5b14d0ab365d060ed7f73de',
        'Cookie': cookie
    }

    content = rq.get(
        # 传入网址参数
        url=home_url,
        headers=headers,

    ).content

    # 写入二进制码 然后转化成json文件
    with open('Data2.json', 'ab') as f:
        f.write(content)

if __name__ == '__main__':
    spdier()