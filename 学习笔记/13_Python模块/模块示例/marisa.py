# 这个模块中，我们将定义角色Marisa，以及她的信息、技能和属性。

# 用全大写的变量名来表示常量，这样可以让代码更容易理解和维护。
MARISA_NAME = "Marisa"
MARISA_HP = 100

# 基础信息
def marisa_info():
    """打印Marisa的基本信息"""
    print(f"角色名: {MARISA_NAME}")
    print(f"生命值: {MARISA_HP}")

# 基础技能
# Defense
def defense():
    """执行Defense技能"""
    print("Marisa释放了Defense！")