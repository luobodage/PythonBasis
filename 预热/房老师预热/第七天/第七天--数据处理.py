import json
"""
@主要实现:打开json文件并且进行数据提取
"""

# 打开json文件
with open('json/Data5.json', 'r', encoding='utf-8') as f:
    # 读取
    content = f.read()
    # 转换成json文件
    content_json = json.loads(content)

# 创建一个csv文件
# with open('data.csv', 'w') as f:
#     f.write('工作Id,工作名字,公司Id,公司名字,薪资')
#     f.write('\n')

# 循环写入 工作id 工作名字 公司id 公司名字 薪资
for i in content_json['content']['positionResult']['result']:
    # print(i)
    with open('data/data.csv', 'a') as f:
        f.write(
            f"{i['positionId']},{i['positionName']},{i['companyId']},{i['companyFullName']},{i['salary']}")
        f.write('\n')
    # print(f"工作Id: {i['positionId']}")
    # print(f"工作名字: {i['positionName']}")
    # print(f"公司Id: {i['companyId']}")
    # print(f"公司名字: {i['companyFullName']}")
    # print(f"公司福利: {i['companyLabelList']}")
    # print(f"薪资: {i['salary']}")
    # print('----------------------------------')
