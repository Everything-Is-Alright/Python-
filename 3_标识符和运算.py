#标识符是程序员在代码中为变量、函数和类等元素所起的名字
#命名规则如下：
#1. 标识符可以由字母、数字和下划线组成
#2. 标识符不能以数字开头
#3. 标识符不能使用Python的关键字，比如if、else、while、for、def、class等
#4. 标识符区分大小写，比如num，Num和NUM是三个不同的标识符

#举个例子。如果我们定义True = 10，print(True),控制台会报错SyntaxError: cannot assign to True

#命名规范，不需要严格遵守，但Python官方推荐使用以下命名规范：
#1. 变量名和函数名使用小写字母，比如my_variable、my_function
#2. 多个部分的变量名和函数名使用下划线分隔，比如my_variable、my_function
#3. 见名知义，比如变量名num表示一个数字，函数名get_name表示获取名字的函数

#现在我们看一个变量相关的案例
#有两个变量a和b，分别赋值为10和20，我们希望交换它们的值
a = 10
b = 20
print("交换前：a =", a, "b =", b)  #输出交换前的值
#交换a和b的值，我们不能直接把a=b，b=a，这样会导致a和b的值都变成20
#我们可以使用一个临时变量temp来交换a和b的值
temp = a
a = b
b = temp
print("交换后：a =", a, "b =", b)  #输出交换后的值