import tushare

#
# str_01 = '大爷，您这是去哪呀？'
# str_02 = '去二仙桥'
#
# str_01.isalpha() # 判断字符串里是否有字母（可以说是中文的文字）
# str_01.isdigit() # 判断字符串里面是否有数字
# str_01.isalnum() # 判断字符串里面是否包含字母或者数字
# str_01.isupper() # 判断字符串里面是否包含大写字母
# str_01.islower() # 判断字符串里面是否包含小写字母
# str_01.isspace() # 判断字符串里面是否包含空格
# str_01.lower() # 把字符串所有的大写字母变成小写字母
# str_01.upper() # 把字符串所有的小写字母变成大写字母
# str_01.index('子字符串') # 返回子字符串最开始出现的位置 可以设置开始值和结束值

str_01 = 'ashdhhhqii'
str_02 = 'ashkjasjkhjkashdhsa'

count = ''
for i in range(len(str_01)):
    for j in range(len(str_02)):
        if str_01[i] == str_02[j] and (str_01[i] not in count):
            count = count + str_01[i]
            number_max = len(count)
            break
if len(count) > number_max:
    number_max = len(count)
print(number_max)
print(count)


ke_daxunfei = tushare.get_hist_data('002230')
ke_daxunfei.to_csv("data.csv")