# 流程控制语句概念
# 流程控制语句（Control Flow Statement）用于控制程序代码的执行顺序。
# 默认情况下，Python 代码是自上而下、逐行顺序执行的；流程控制语句可以改变这种顺序。
# 例如：if 语句根据条件决定是否执行某段代码；for 循环让某段代码重复执行多次。
# Python 基础流程控制按功能大致可分为以下几类：
#   1. 顺序结构（天然默认，无需特殊语句）
#   2. 条件（分支）结构：if / elif / else
#   3. 循环结构：while、for
#   4. 循环控制语句：break、continue、pass

# 顺序结构（Sequential Structure）
# 程序默认的执行方式：从上到下，一条一条依次执行，不跳转、不重复。
# Python 没有类似其他语言的顺序结构关键字，它就是"什么都不写"的默认行为。
# 【举个例子】
print("魔理沙")
print("灵梦")
print("东风谷早苗")

# 【注意事项】
#   1. 顺序结构是默认行为，需要改变它时才用到分支或循环。
#   2. 语句的执行顺序 = 书写顺序（同一缩进层级内）。

# 条件（分支）结构（if / elif / else）
# 条件结构根据条件的真假，选择性地执行不同的代码块。
#   if 条件:        条件为真时执行
#   elif 条件:      前面都不成立，且当前条件为真时执行（可多个）
#   else:           前面所有条件都不成立时执行（可选，最多一个）
# 关键语法点：
#   - if 后面的表达式会被真值测试（truthy / falsy）。
#   - 每个分支末尾有冒号 :，下一行起必须缩进，否则会被判定为直接打印。
#   - 分支是"互斥"的：一旦某个分支命中，其余分支不再判断。
#   - 三元表达式（条件表达式）：a if 条件 else b，用于简单赋值。
# 基本格式：
# if 判断条件:
#   条件成立时执行的操作
# 【举个例子】
money = int(input("请输入钱数："))
if money >= 69:
    print("你可以玩红魔乡新典")
elif money >= 38:
    print("你可以玩夜雀食堂")
elif money >= 9:
    print("你可以玩baka")
else:
    print("你就是baka")
    print("bakabakabakabakabakabaka")

#对于作为一个整体的条件，可以用()将其括起来，这一点适用于同时需要多个判断的条件
#比如判断闰年
year = int(input("请输入年份："))
if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print("你输入的年份是闰年")
else:
    print("你输入的年份不是闰年")

# 三元表达式示例
level = "不是baka" if 9 <= money <= 69 else "是baka"
print("等级：", level)

# 【注意事项】
#   1. Python 靠"缩进"划分代码块，缩进必须统一（推荐 4 个空格），否则报 IndentationError。
#   2. 不要写 if x == True:，直接写 if x: 即可。
#   3. elif 是 else if 的缩写，不能单独使用，必须跟在 if 后面。
#   4. 三元表达式适合简单场景，逻辑复杂时仍用普通 if 更易读。

# 模式匹配（match……case）
# 模式匹配就是用一个清晰的模板去匹配数据的结构和内容，匹配成功则执行相应的操作
# 其实就是switch……case
#   match:        计算指定表达式的值
#   case:         前面都不成立，且当前条件的值匹配时执行（可多个）
# 基本格式：
# switch 变量:
#   case "1"：
#       条件成立时执行的操作
#   case "2":
#       条件成立时执行的操作
#   case "3":
#       条件成立时执行的操作
#   case _:
#       条件成立时执行的操作
# case_用于匹配其他所有情况，类似于if……else中的else
# 【举个例子】
name = input("请输入角色名称：")
match name:
    case "魔理沙":
        print("她住在魔法森林")
    case "灵梦":
        print("她住在博丽神社")
    case "蕾米莉亚":
        print("她住在homo馆")
    # 多种情况对应同一个执行操作，可以用case "1" | "2"
    case "古明地觉" | "古明地恋":
        print("她住在地灵殿")
    # 针对于需要判断的情况，可以在判断后加入一个if条件判断作为补丁
    # 例如针对num1 / num2 的情况，如果num2 == 0，就会出现报错
    # case "/" if num != 0:
    case _:
        print("我也不知道她住在哪里")


# while 循环（While Loop）
# while 循环在条件为真时反复执行代码块，直到条件为假才停止。
#   while 条件:
#       循环体
# 关键语法点：
#   - 每次执行循环体前都会重新判断条件，为真才继续。
#   - 条件一开始就为假时，循环体一次都不会执行。
#   - 必须有"使条件趋向为假"的代码，否则会死循环。
#   - 常配合 else：当循环"正常结束"（非 break 结束）时执行 else 块。
# 【举个例子】
count = int(input("请输入count值："))
total = 0
while count <= 5:
    total += count
    print(f"第 {count} 次累加，当前总和 = {total}")
    count += 1
print("最终总和 =", total)

# while ... else 示例
n = 3                                                                                                                                                                                                     
while n > 0:
    print("n =", n)
    n -= 1
else:
    print("循环正常结束，执行 else 分支")

# 【注意事项】
#   1. 忘记更新循环变量会导致死循环，务必确保条件最终会变为假。
#   2. while 的 else 分支在循环被 break 时不会执行。
#   3. 条件恒为真（while True）可做无限循环，需要配合 break 退出。
#   4. 浮点数用作循环条件慎用 == 判断，可能因精度永不满足而无限循环。

# for 循环（For Loop）
# for 循环用于"遍历"一个可迭代对象（Iterable），如字符串、列表、元组、字典、range。
#   for 变量 in 可迭代对象:
#       循环体
# 关键语法点：
#   - range(start, stop, step)：生成整数序列，stop 不包含，step 可为负。
#   - 遍历字典默认遍历"键"；.items() 遍历键值对；.keys()/.values() 同理。
#   - 常配合 else：当循环"正常结束"（非 break 结束）时执行 else 块。
#   - 常用于列表推导式前的入门理解：for 是迭代的核心。
# 【举个例子】
# 遍历 range
for i in range(1, 6):
    print("range 遍历 i =", i) 

# 遍历字符串
msg = "我是东风谷早苗"
for i in msg:
    print(i)

# 遍历列表
character = ["以撒", "夏娃", "阿萨泻勒"]
for name in character:
    print("角色：", name)

# 遍历字典的键值对
person = {"name": "八云紫", "age": 1145141919810}
for key, value in person.items():
    print(f"{key} -> {value}")

# for ... else 示例
for i in range(3):
    print("循环 i =", i)
else:
    print("for 循环正常结束，执行 else 分支")

# 【注意事项】
#   1. 遍历时修改被遍历的对象可能导致意料之外的结果，建议遍历副本或另建容器。
#   2. range 的 stop 参数不包含，range(5) 是 0,1,2,3,4。
#   3. for 的 else 分支在循环被 break 时不会执行。
#   4. for 循环变量在循环结束后仍会保留最后一次的值，不会自动销毁。

# 循环控制语句（break / continue / pass）
# 用于精细控制循环的执行流程。
#   break     立即终止整个循环，跳出循环（不再执行剩余迭代与 else）。
#   continue  跳过本次迭代的剩余代码，直接进入下一次迭代。
#   pass      空语句，占位用，不做任何事（保持语法完整）。
# 【举个例子】
# break 示例：找到目标就停止
for i in range(1, 10):
    if i == 5:
        print("找到 5，提前结束循环")
        break
    print("当前 i =", i)

# continue 示例：跳过偶数
print("--- 只打印奇数 ---")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print("奇数：", i)

# pass 示例：占位
for i in range(3):
    if i == 1:
        pass   # 先占位，以后再补充逻辑
    print("i =", i)

# 【注意事项】
#   1. break 一旦执行，循环的 else 分支不会执行。
#   2. continue 在 while 中要小心：若更新语句在 continue 之后，会导致死循环。
#   3. break / continue 只作用于"最内层"循环，多重循环中要跳出需用标志位或函数返回。
#   4. pass 不是注释，它是真正执行的空语句，常用于函数/类/分支占位。



# while 与 for 的使用场景
# while 用于在某个特定条件满足时一直循环，循环的次数通常是未知的，只知道循环开始、结束的条件（关注的是循环的条件）
# for 用于对一个已知数据集进行遍历，或已知循环次数的循环（关注的是遍历每一个元素）



# 循环的嵌套（Nested Loops）
# 在一个循环内部再写另一个循环，形成嵌套结构，常用于二维数据处理。
# 关键语法点：
#   - 外层循环走一次，内层循环完整走一遍。
#   - 内层 break / continue 只影响内层循环。
#   - 常配合嵌套推导式（如 [[...] for ... for ...]）。
# 【举个例子】
for i in range(1, 4):          # 外层：行
    for j in range(1, 4):      # 内层：列
        print(f"{i} * {j} = {i * j}", end="\t")
    print()   # 每行结束后换行，空字符串会被定义为\n，即换行符

# 【注意事项】
#   1. 嵌套层数过多会降低可读性与性能，一般不超过 3 层。
#   2. 跳出外层循环需借助标志变量、函数 return 或异常。
#   3. 注意内层循环的循环变量与外层不要重名，避免混淆。










# 【补充】
# range语句
# range语句用于生成指定规则的数字序列

# 用法1：range(end)  获取一个从0开始，到end结束的数字序列（不包括end本身）
# range(5)  获取数据：0，1，2，3，4

# 用法2：range(start,end)  获取一个从start开始，到end结束的数字序列（不包含end本身）
# range(2,10)  获取数据：2，3，4，5，6，7，8，9

# 用法3：range(start,end,step)  获取一个从start开始，到end结束的数字序列，step步长（不包含end本身）
# range(2,12,3)  获取数据：2，5，8，11





# 【拓展】循环控制与可迭代协议
# Python 的 for 循环底层依赖"可迭代协议"（__iter__ / __next__）。
# 理解 apply 于自定义对象时，就能解释为什么 for 能遍历它们。
#   迭代对象（Iterable）：实现了 __iter__，可被 for 遍历。
#   迭代器（Iterator）：实现了 __iter__ 和 __next__，是真正逐次取值的对象。
#   生成器（Generator）：用 yield 产生，天生就是迭代器。
# 【举个例子】
def my_gen():
    yield 1
    yield 2
    yield 3

for value in my_gen():
    print("生成器值：", value)

# 【注意事项】
#   1. 迭代器是"一次性"的，遍历完就耗尽，再次遍历不会从头开始。
#   2. 用 iter() 得到迭代器，用 next() 逐个取值，取尽抛 StopIteration。
#   3. 生成器惰性求值，节省内存，适合处理大数据流。

# 流程控制综合优先级与执行顺序（注意事项汇总）
#   1. 分支判断是"从上到下、命中即止"，条件顺序会影响结果与性能（高频条件放前面）。
#   2. 循环中尽量减少不必要的重复计算，可提到循环外。
#   3. break / continue / pass 的语义要分清：终止 / 跳过 / 占位。
#   4. 循环与 else 是 Python 特色：只有"非 break 正常结束"才执行 else。
#   5. 缩进即语法，统一使用 4 个空格，避免 Tab 与空格混用。
