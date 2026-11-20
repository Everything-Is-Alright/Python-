# 多态是指同一个方法具有不同的形态、行为、表现
class Human:
    def __init__(self, h_name, h_hp, h_hobby):
        self.name = h_name
        self.hp = h_hp
        self.hobby = h_hobby

    def need(self):
        print(f"{self.name}的生命需要食物、空气和爱来维持！")

class Monster(Human):
    def need(self):
        print(f"{self.name}的生命需要死亡、痛苦和荣耀（存疑）来维持！")

class God(Human):
    def need(self):
        print(f"{self.name}的神力需要信仰与祷告来维持！")

# 我们来定义一个函数，询问他们的需求
# 函数的参数类型为父类，支持传入任意子类，而不必对函数进行修改
def what_is_you_need(character: Human):
    character.need()

marisa = Human("marsia", 100, "Magic")
cirno = Monster("cirno", 80, "frog")
suwako_moriya = God("suwako_moriya", 90, "faith")

what_is_you_need(marisa)
what_is_you_need(cirno)
what_is_you_need(suwako_moriya)

print("----------------------------------------------------")
# 对了，依旧，命名只是用于阅读的便利性，你仍然可以
# def what_is_you_need(character):
# 这样依旧会根据你传入的对象动态地进行识别

# 多态-鸭子类型
# 鸭子类型是指，如果它走路像鸭子，叫起来像鸭子，那可以认为它就是鸭子——就算它是鸡，或者老鼠。
# 在鸭子类型中，我们不关注对象的类型，而是关注对象的行为。
class Khorme():
    def Roar(self):
        print("血祭血神，颅献颅座！")

class Tzeentch():
    def Roar(self):
        print("赞美万变之主！")

class Nurgle():
    def Roar(self):
        print("盛大的传疫巡游开幕！")

class Slaanesh():
    def Roar(self):
        print("114514！")

def war_roar(soilder):
    soilder.Roar()

k = Khorme()
t = Tzeentch()
n = Nurgle()
s = Slaanesh()
war_roar(k)
war_roar(t)
war_roar(n)
war_roar(s)
# 所以事实上，鸭子类型是不依赖继承的多态，python中大部分多态也都是鸭子类型，不太依赖继承体系。