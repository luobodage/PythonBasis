import tushare as ts

pro = ts.pro_api("6087fa93219ccca28b924ee72ce6940025cd0fe83280245f924e6385")

# 获取美国新冠状肺炎疫情感染统计人数
df = pro.ncov_global(country='美国', fields='country,publish_date,confirmed_num,update_time')

df.to_csv('中国疫情.csv')