# 这个模块中，我们将定义角色Reimu，以及她的信息、技能和属性。

REIMU_NAME = "Reimu"
REIMU_HP = 100

# 基础信息
def reimu_info():
    """打印Reimu的基本信息"""
    print(f"角色名: {REIMU_NAME}")
    print(f"生命值: {REIMU_HP}")

# 基础技能
# Attack
def attack():
    """执行攻击技能"""
    print("Reimu释放了梦想封印！")