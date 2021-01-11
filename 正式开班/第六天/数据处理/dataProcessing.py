import pandas as pd
import time

start = time.time()

#long running

data = pd.read_excel('housing.xls') # 读取xls文件
pd.set_option('display.width',None) # 设置中间不省略
print(data.head())
max_rooms = max(list(data['total_rooms']))

print([i for i in data[data.total_rooms == max_rooms]['median_income']][0])

end = time.time()

print(end-start)