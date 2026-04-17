# 1. 函数也是对象
a1 = 100  # int 类de实例对象
a2 = '字符串'  # str 类de实例对象
a3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # list 类de实例对象
def make_sound(): #  function 类de实例对象
    print('说话')
print(type(a1))
print(type(a2))
print(type(a3))
print(type(make_sound))

# 2. 函数可以动态添加属性
def greet():
    print("Hello!")
greet.author = "Alice"
greet.version = 1.0
print(greet.author)  # 输出：Alice
print(greet.version)  # 输出：1.0

# 3. 函数可以赋值给变量
def greet2():
    print("Hello! 函数可以赋值给变量")
# 赋值给变量
say_hello = greet2
say_hello()  # 输出：Hello!函数可以赋值给变量（通过变量调用函数）

# 4. 可变参数 vs 不可变参数
def modify_args(a, b):
    # 不可变参数（数字）：修改不会影响外部
    a += 1
    # 可变参数（列表）：修改会影响外部
    b.append(4)
    print(f"函数内：a={a}, b={b}")
x = 10
y = [1, 2, 3]
modify_args(x, y)
print(f"函数外：x={x}, y={y}")  # 输出：函数外：x=10, y=[1, 2, 3, 4]

# 5. 函数也可以作为参数
def add(a, b):
    return a + b
def calculate(func, x, y):
    return func(x, y)
result = calculate(add, 3, 5)
print(result)  # 输出：8

# 6. 函数也可以作为返回值
def make_adder(n):
    def adder(x):
        return x + n
    return adder  # 返回内部定义的函数

add_5 = make_adder(5)
print(add_5(3))  # 输出：8（3 + 5）
add_10 = make_adder(10)
print(add_10(3))  # 输出：13（3 + 10）