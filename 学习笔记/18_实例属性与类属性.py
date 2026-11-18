# 实例属性与类属性
# 实例属性：属于每个具体对象的属性，每个对象都是独立的。（各个对象特有的数据）
# 类属性：属于类本身的属性，所有的实例共享。（所有对象共享数据或配置）

# 其实，这两个概念可以类比为java中的静态变量和非静态变量
# 类属性就是有static关键字修饰的静态变量，而实例属性就是没有static修饰的非静态变量

# 举个例子
class Troop:
    # 以下两个属性，占用位置和补员速率，就是类属性
    # 所有的兵牌实例都会占用队伍中的1个位置，每回合补员50%
    space = 1
    replenish = 0.5

    # 在下面的name，hp和count就是实例属性
    # 不同单位可以有自己的名字：天庭龙弩，万变魔君，惊惧兽
    # 不同单位可以有自己的生命值：10000，6400，8080
    # 不同单位可以有自己的兵模数量：1，120，32
    def __init__(self, t_name, t_hp, t_count):
        self.name = t_name
        self.hp = t_hp
        self.count = t_count

    def recruit(self):
        print(f"{self.name}完成招募！")

    def unit_hp(self):
        return self.hp / self.count

    def total_hp(self, t_total_count):
        return self.hp * t_total_count

# 通过实例查找属性时，会先查找实例属性，实例属性不存在时，在查找类属性。 