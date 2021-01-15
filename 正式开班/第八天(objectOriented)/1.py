"""
author: luoboovo
contact: fuyu16032001@gmail.com
datetime:2021/1/13 15:09
software: PyCharm
"""
"""
codeFunction:
"""


class WumingFeng():
    # def __init__(self, thMa, quantity, *args):
    #     self.thMa = thMa
    #     self.quantity = quantity
    #     self.args = args

    def __init__(self, thMa, quantity, likesoup):
        self.thMa = thMa
        self.quantity = quantity
        self.likesoup = likesoup



    def mian1(self, n):
        print(self.thMa, self.quantity, self.likesoup, n)

    def mian(self):
        self.thMa = input("输入要吃的面码")
        self.quantity = int(input("要吃几两面"))
        self.args = input("是否带汤")
        print("加了", self.thMa, "粉", self.quantity, "两", "是否带汤", self.args)


f1 = WumingFeng("鸡肉", 3, 2)
f1.mian1(1)
f2 = WumingFeng("牛肉", 2, "不加青菜")
f2.mian()
