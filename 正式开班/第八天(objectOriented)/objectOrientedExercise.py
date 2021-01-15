# author:luoboovo
# contact: fuyu16001@gmail.com
# datetime:2021/1/13 9:56
# software: PyCharm

# 1.	定义一个汽车类（Car），属性有颜色，品牌，车牌号，价格，并实例化两个对象，给属性赋值，并输入属性值
class Car:
    def __init__(self, color, brandCar, trademark, price):
        self.color = color
        self.brandCar = brandCar
        self.trademark = trademark
        self.price = price


c = Car('红色', '奔驰', '123', 599999)
print(c.price)


# 2.	定义一个球员类(Player)，属性有身高，体重，姓名，实例化两个球员，分别是姚明和科比；
class Player:
    def __init__(self, height, bodyWeight, name):
        self.height = height
        self.bbodyWeight = bodyWeight
        self.name = name


c = Player(180, 75, '科比')
c2 = Player(200, 75, '姚明')
print(c.name)
print(c2.name)


# 3.	定义一个僵尸类(Zombie)，属性有名子，体力值，攻击力，实例化三个僵尸类，并给属性赋值；
class Zombie:
    def __init__(self, name, stamina, attackPower):
        self.name = name
        self.stamina = stamina
        self.attackPower = attackPower

    def __str__(self) -> str:
        return super().__str__()


z1 = Zombie('铁通僵尸', 100, 200)
z2 = Zombie('撑杆跳僵尸', 100, 200)
z3 = Zombie('铁门僵尸', 100, 200)
