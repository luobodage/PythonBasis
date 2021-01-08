# 导入easyocr
import easyocr
import requests

# 创建reader对象
url = input('请输入你要识别的图片地址:')
img_path = 'image/image.jpg'


def getPictures():
    """
    获取图片二进制码
    :return: 返回值为二进制码
    """
    content = requests.get(
        url=url
    ).content
    return content


def OCRdistinguish():
    reader = easyocr.Reader(['ch_sim', 'en'])
    # 读取图像
    result = reader.readtext(img_path)
    print(result)


if __name__ == '__main__':
    # 写入二进制代码 并且生成.jpg文件
    with open(img_path, 'wb') as f:
        f.write(getPictures())
    OCRdistinguish()
