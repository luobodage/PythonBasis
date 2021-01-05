import pandas as pd

"""
@主要实现:整理薪资的格式 把'3k-5k'这种格式变成(3000+5000)/2
"""

# 文件路径
csv_path = 'data/data.csv'
# 数据读取
data = pd.read_csv(csv_path, encoding='gb18030', error_bad_lines=False)
xinxi_list = list(data['薪资'])
data_xinzi = []
for i in xinxi_list:
    data_xinzi.append(int((float(i.split('-')[0]) + float(i.split('-')[1])) / 2 * 1000))

print(data_xinzi)
data['薪资'] = data_xinzi

data.to_csv('data_modfiy.csv')
