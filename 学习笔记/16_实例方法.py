# 在类中定义方法，与之前定义函数的方式没有太大差别

# 先定义一个兵种类
class Troop:
    def __init__(self, t_name, t_hp, t_count):
        self.name = t_name
        self.hp = t_hp
        self.count = t_count

    # 让我们给这个兵种加一个招募完成的提示
    def recruit(self):
        print(f"{self.name}完成招募！")

    # 现在我们根据这个兵种的属性计算单个兵模的血量
    def unit_hp(self):
        return self.hp / self.count

    # 计算一下如果出了多个该兵种的兵牌，能提供的总血量
    def total_hp(self, t_total_count):
        return self.hp * t_total_count

nurglings = Troop("纳垢灵", 8400, 60)
# 先来看看招募完成了没
nurglings.recruit()
# 看来纳垢灵已经招募完成，我们来看看每一只纳垢灵的生命值
nurglings_unit_hp = nurglings.unit_hp()
print(f"单个兵模血量为{nurglings_unit_hp}")
# 我们招募了3队纳垢灵，它们能给我们领主提供多少血量呢
print(f"{nurglings.name}能为部队提供{nurglings.total_hp(3)}点血量")