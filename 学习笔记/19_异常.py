# 异常，也成为bug，是程序运行过程中出现的错误，它会终端程序的正常执行流程
# 异常的作用：
# 保证数据、逻辑的正确性，避免程序执行混乱。‘
# 在开发阶段尽可能发现更多问题，尽早解决问题，保证程序正常运行

# 程序中出现异常有两种处理方案：
# 1.不做处理：整个程序会因为一个bug而中断执行。我们之前写的程序都没有做异常处理，所以有bug就中断了。
# 2.捕获异常：按照我们自己的处理方式处理异常，让程序继续运行。（编写程序时做好预案，出现异常时按预案处理）

# 异常的捕获
# try:
#    可能出现异常的业务代码1
#    可能出现异常的业务代码2
#    ……
# except 异常类型 as 变量名:
#    出现异常的预案
# finally:
#    不管是否出现异常，都会执行的代码
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

nurglings = Troop("纳垢灵", 8400, 0)

try:
    print(nurglings.unit_hp())
except ZeroDivisionError as e:
    print("程序运行报错，错误信息：",e)
finally:
    print("释放资源！")