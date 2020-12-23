import requests

# 微信的app用户id以及用户验证码
appid = 'wx0ad91edb67ead7bd'
secret = 'a19e9072c5ab070cc9ab666680f6b026'


def hq_token():
    # 获取token 两个小时一刷新
    url_token = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
    content = requests.get(url_token)
    # 获取token以及时间
    global token
    token = content.json()['access_token']
    # 获取tag地址
    url_get_tag = f'https://api.weixin.qq.com/cgi-bin/tags/get?access_token={token}'
    requests.get(url_get_tag)
    print('-----------------------------------------')


def post_cr(name):  # 传入数据
    """
    :return:传入数据
    """
    # post接口
    url_post_tag = f'https://api.weixin.qq.com/cgi-bin/tags/create?access_token={token}'
    # 要上传的数据
    data = {'tag': {'name': name}}
    # 传入json数据
    requests.post(url=url_post_tag, json=data)
    print('-----------------------------------------')


# 输出json格式数据

# assert 0 == content_tag_json['tags'][0]['count']

# assert 'cfy4' == content_tag_post.json()['tag']['name']

def get():
    url_post_tag_get = f'https://api.weixin.qq.com/cgi-bin/tags/get?access_token={token}'
    global content_tag_get
    content_tag_get = requests.get(url=url_post_tag_get)

    # 循环遍历
    for i in content_tag_get.json()['tags']:
        print(i)
    print('-----------------------------------------')


def update(id, name):
    url_post_tag_update = f'https://api.weixin.qq.com/cgi-bin/tags/update?access_token={token}'

    # data_update = {'tag': {'id': content_tag_get.json()['tags'][1]['id'], 'name': 'cfylalalalala'}}
    data_update = {'tag': {'id': id, 'name': name}}
    requests.post(url=url_post_tag_update, json=data_update)
    # assert 'cfylalalalala' == content_tag_get.json()['tags'][1]['name']
    get()
    print('-----------------------------------------')


def delete(number):
    url_post_tag_delete = f'https://api.weixin.qq.com/cgi-bin/tags/delete?access_token={token}'
    data_delete = {'tag': {'id': number}}
    requests.post(url=url_post_tag_delete, json=data_delete)
    get()
    print('-----------------------------------------')


if __name__ == '__main__':
    hq_token()  # 获取token
    get()  # 查看当前服务器内容
    update(103, 'daweitianlong!')  # 修改
    post_cr('cfy82')  # 添加
    delete(106)  # 按照id编号删除
