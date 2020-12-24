import requests

# home_url = 'https://search.jd.com/Search?keyword=%E5%9C%A3%E8%AF%9E%E7%A4%BC%E7%89%A9&enc=utf-8&wq=sheng%27dan&pvid=7b26c3ef3287492b9bf7990154ac6a63'


img_url = 'http://img14.360buyimg.com/n7/jfs/t1/152825/38/10944/164600/5fe218ccE42ca9ff7/d8452f0d20a33f15.jpg'

content = requests.get(
    url=img_url
).content

with open('jd_img.jpg', 'wb') as f:
    f.write(content)
