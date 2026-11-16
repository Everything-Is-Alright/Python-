# 导入模块
import random
import math as m
from math import sqrt as square_root


# 使用random模块生成10个1~100之间的随机整数
for i in range(10):
    num = random.randint(1, 100)
    print(num)

# 使用math模块计算16的平方根
result = m.sqrt(16)
print(result)  # 输出结果为4.0

# 使用math模块计算25的平方根
result2 = square_root(25)
print(result2)  # 输出结果为5.0