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