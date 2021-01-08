list_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(2):
    a = int(input("请输入你要插入的数字:"))
    list_8.append(a)
print(list_8)
b = int(input("请输入你要删除的数字的位置:"))
del list_8[b - 1]
print(list_8)
