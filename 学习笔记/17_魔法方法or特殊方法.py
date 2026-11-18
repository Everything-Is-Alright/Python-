# 魔法方法/特殊方法是指python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，如__init__
# 魔法方法是不需要我们手动调用的，Python会在合适的时机自动调用

# 常见的魔法方法

# __init__: 初始化方法
# __str__: 字符串表示的方法
# __eq__: 比较两个对象是否相等
# __lt__, __le__, __gt__, __ge__: 比较两个对象的大小，小于（less than）、小于等于（less than or equal）、大于（greater than）、大于等于（greater than or equal）

# 我们继续用兵种类
class Troop:
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

    # 我们需要给这个类加入魔法方法
    # __str__会将属性转为字符串输出，而非地址值
    def __str__(self):
        return f"名称：{self.name}, 血量：{self.hp}, 兵模数量：{self.count}"

    # 想要对比两个单位，可以使用self与other
    def __eq__(self, other):
        return self.name == other.name and self.hp == other.hp and self.count == other.count
    # 再对比一下两个单位的生命值比较
    def __lt__(self, other):
        return self.hp < other.hp
nurglings = Troop("纳垢灵", 8400, 60)
peasant_archers = Troop("役农弓手", 6480, 120)

# 这种情况下打印两个实例，就会显示其定义的具体信息，而非地址
print(nurglings)
print(peasant_archers)

# 如果想要对比两个单位，直接使用==是不行的，因为这样对比的仅仅是地址
print(f"两个单位地址对比：{nurglings == peasant_archers}")
print("----------------------------------------")

# 输出两个单位的属性
print(f"{nurglings.name}的属性为{nurglings.__str__()}")
print(f"{peasant_archers.name}的属性为{peasant_archers.__str__()}")

# 判断这两个单位是不是同一单位
print(f"两单位是否是同一单位：{nurglings.__eq__(peasant_archers)}")

# 判断纳垢灵血量是否高于役农弓手
if peasant_archers.__lt__(nurglings):
    print(f"{nurglings.name}的生命值高于{peasant_archers.name}")
elif nurglings.__lt__(peasant_archers):
    print(f"{peasant_archers.name}的生命值高于{nurglings.name}")
else:
    print("两个兵种生命值相同！")