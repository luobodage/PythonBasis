import pandas as pd

# 获取数据库数据
userInfo = pd.read_csv('userInfo.csv')

print(userInfo)


username = '小鱼鱼'

print(int(userInfo.loc[userInfo['username'] == username, 'accountStatus']))
userInfo.loc[userInfo['username'] == username, 'accountBalance'] = int(
            userInfo.loc[userInfo['username'] == username, 'accountBalance']) + 100
print(userInfo)
# print(userInfo)
# print(userInfo.loc[userInfo['username'] == username, 'accountStatus'])

# user_account = userInfo[userInfo.username == username]
# user_account['accountStatus'][0] = 0
# print(user_account)

# print(userInfo.loc[username])
# print(userInfo[userInfo.username == username])
# print(list(userInfo[userInfo.username == username][0:1]))


# for i in range(len(userInfo['username'])):
#     if userInfo['username'][i] == '小萝卜':
#         print(userInfo.iloc[i].at['accountStatus'])
#
# print([userInfo.iloc[i].at['accountStatus'] for i in range(len(userInfo['username']))  if userInfo['username'][i] == username][0])


