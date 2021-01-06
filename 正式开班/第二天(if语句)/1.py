print("-----------------------------------------")
print("打印某年某月有多少天。（提示：A、闰年的计算方法：年数能被4整除，并且不能被100整除；或者能被400整除的整数年份。")
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
# month_day = {
#     1: 31,
#     3: 31,
#     5: 31,
#     7: 31,
#     8: 31,
#     10: 31,
#     12: 31,
#     4: 30,
#     6: 30,
#     9: 30,
#     11: 30
# }
month_day = {
    31: (1, 3, 5, 7, 8, 10, 12),
    30: (4, 6, 9, 11)
}
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year}年{month}月有29天哦~")
    else:
        print(f"{year}年{month}月有28天哦~")
else:
    if month in month_day[31]:
        print(f"{year}年{month}月有31天哦~")
    else:
        print(f"{year}年{month}月有30天哦~")