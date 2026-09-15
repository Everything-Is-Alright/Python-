#常见的基础数据类型
#1. 数字类型（int, float, complex）
#2. 字符串类型（str）
#3. 布尔类型（bool）
#4. 空值类型（NoneType）

#虽然Python是一种动态类型语言，但我们仍然可以使用type()函数来查看变量的类型
name = "魔理沙"  #定义一个字符串变量name，并赋值为"魔理沙"
print(type(name))  #输出变量name的类型
num = 3.14  #定义一个浮点数变量num，并赋值为3.14
print(type(num))  #输出变量num的类型
#也可以直接查看具体的字面量类型
print(type(18))  #输出整数18的类型
print(type(True))  #输出布尔值True的类型
print(type(None))  #输出空值None的类型

#我们也可以用isinstance()函数来判断一个变量是否是某个类型的实例，这个函数将返回True或False
print(isinstance(name, str))  #判断变量name是否是字符串类型的实例
print(isinstance(num, float))  #判断变量num是否是浮点数类型的实例
print(isinstance(True, bool))  #判断变量True是否是布尔类型的实例
print(isinstance(None, type(None)))  #判断变量None是否是空值类型的实例