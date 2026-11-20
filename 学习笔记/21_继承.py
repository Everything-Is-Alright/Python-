# 继承描述的是两个类之间的关系，子类继承父类，就可以获取到父类的属性和方法。（非私有）
# 所有的类都有一个父类，如果不指定，其父类就是Object。类比为monobehavier，万物之基类。

# 我们先定义一个人类
class Human:
    #__init__方法并非私有的，所以在继承中可以被正常继承
    def __init__(self, h_name, h_hp, h_hobby):
        self.name = h_name
        self.hp = h_hp
        self.hobby = h_hobby

    def __str__(self):
        return f"角色名称：{self.name}, 角色生命值：{self.hp}, 角色爱好：{self.hobby}"

    def show_type(self):
        print(f"{self.name}是一名人类！")

    def need(self):
        print("人类的生命需要食物、空气和爱来维持！")

# 现在我们想定义一个妖怪类，不过妖怪类有一些属性与人类相同，这里就可以使用继承
class Monster(Human):
    pass

marisa = Human("marisa", 100, "alice")
cirno = Monster("cirno", 50, "frog")

print(marisa)
print(cirno)

# 从父类继承的方法可以进行重写
# 重写是指子类继承父类后，如果父类中方法不满足需求，可以在子类中重新定义父类中已有的方法（方法名相同），从而用子类的实现替换掉父类的实现。
# 现在我们想定义一个神明类，同样可以继承自人类，可能这是个古希腊神明吧

print("--------------------------------------")

class God(Human):
    # 直接在子类中重写
    def show_type(self):
        print(f"{self.name}是一位神明！")

    # 如果在子类中重写父类方法时，需要调用父类的方法，可以通过父类名.方法名(self)，或者super().方法名()的方式来进行调用。
    def need(self):
        super().need()
        Human.need(self)
        print("而神明的神力只依仗人们的信仰！")
nyarlathotep = God("nayrlathotep", 129890384148359029790182904882149, "???????")

print(nyarlathotep)

marisa.show_type()
nyarlathotep.show_type()

marisa.need()
nyarlathotep.need()

# 多继承
# 在python中，一个子类可以同时继承多个父类，一个父类也可以被多个子类继承
# 多继承就是指一个子类同时继承了多个父类的情况，这回让子类将多个父类中的非私有属性和方法都会继承下来。
class Ghost:
    def __init__(self, g_name, g_hp, g_hobby):
            self.name = g_name
            self.hp = g_hp
            self.hobby = g_hobby

    def show_type(self):
        print(f"{self.name}是一名幽灵！")

# 假设某类人既有Human又有Ghost的属性和功能，就可以使用多继承
# 不过这也引申出一个问题：如果多个父类有同名的属性或方法，会如何调用呢
# 可以使用 类名.__mro__.属性 或 类名.mro() 方法查看调用顺序
class Youmu(Human, Ghost):
    pass

youmu = Youmu("youmu", 120, "太刀")
youmu.show_type()
# 看来youmu是一位人类
# 按照“方法解析顺序”(MRO原则)，会先运行第一个父类中的方法

# 如果我们想让youmu调用Ghost类中的方法，我们可以直接在类中进行重写，在重写里使用你需要的方法。
