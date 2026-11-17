# 定义一个类
# 类遵循大驼峰命名法，每个单词的首字母大写，单词之间没有分隔符。
# 譬如Human，HumanAbility
class Human:
    # 我们先用一个空结构，使用关键字class
    pass

# 创建对象
# 让我们创建一个名叫Marisa的人类
marisa = Human()

# 动态地为对象添加属性
# 报错不用担心，运行时会自动创建属性
marisa.age = 18
marisa.hp = 100
marisa.bp = 30
marisa.skill = "极限火花"

# 直接打印marisa，输出的是一个地址。想看到具体属性，可以使用__dict__
# 这个关键字会将对象的所有属性以字典的形式输出出来。
print(marisa)
print(marisa.__dict__)


# 不建议在类之外动态添加属性方法，而是在定义类时指定，以此提高类的可读性。
# 对于“方法”，定义在类之外的成为函数，而定义在类之内的称之为方法。
# __init__是一个初始化方法，对象创建后自动调用，主要用于设置对象的初始状态（设置对象属性）
# self是方法的第一个参数，表示当前创建的实例对象（相当于java中的this），即我们将要基于此类创建出的实例，必须放在初始化方法的第一位。
# self后是参数列表，在这里定义多少个参数，在后面实例化时就要指定多少个参数。

# 举个例子，我们来定义一个兵牌类
# 我们将赋予兵牌名称、血量与单位数量三个属性。
print("--------------------------------------------")
class Troop:
    def __init__(self, t_name, t_hp, t_count):
        self.name = t_name
        self.hp = t_hp
        self.count = t_count

# 创建一个兵牌实例
# 我们只用传递三个属性即可，self不需要
exalted_bloodreaper = Troop("怒狂者", 10080, 32)
print(exalted_bloodreaper.__dict__)