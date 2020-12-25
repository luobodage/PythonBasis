import base64
from aip import AipFace

APP_ID = '17759762'
API_KEY = 'PaG6u8bpFPXgpXaXGz3n3rUL'
SECRET_KEY = 'XjAPFmh7huv4k80Xynmj8GB78VZ8Rjhw'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 人脸对比
def face_detect(filepath1, filepath2):
    result = client.match([
        {
            'image': str(base64.b64encode(open(filepath1, 'rb').read()), 'utf-8'),
            'image_type': 'BASE64',
            'face_type': 'LIVE',
        },
        {
            'image': str(base64.b64encode(open(filepath2, 'rb').read()), 'utf-8'),
            'image_type': 'BASE64',
            'face_type': 'LIVE',
        }
    ])
    # print(result)  # 打印出所有的信息
    a = result['result']['score']
    # print(a)  # 单独显示出相似度 其他的类似
    if a >= 80:
        print('这是一个人哦~')
    else:
        print('这不是一个人哦')


# 人脸库增加 地址 组 用户
def face_add(filepath, unit, num):
    with open(filepath, 'rb') as fp:
        image = image = base64.b64encode(fp.read())
    imageType = "BASE64"
    groupid = unit
    userid = num
    result = client.addUser(image, imageType, groupid, userid)
    if result['error_code'] == 0:
        print('增加人脸成功')
    else:
        print("增加人脸失败")


# 删除人脸库
def face_delete(filepath):
    userId = "用户名称"
    groupId = "用户组名称"
    result = client.deleteUser(groupId, userId)  # 其实这里不用按照官方的demo三个参数 每张照片单独的token不用也可以的！
    print(result)
    if result['error_code'] == 0:
        print("删除人脸成功")
    else:
        print("删除人脸失败")


if __name__ == '__main__':
    face_detect('1.jpg', 'songxiaobao2.jpg')

