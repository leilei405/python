def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    return add, subtract, multiply, divide  # 自动打包为元组

# 调用函数并接收多个返回值
result = calculate(10, 5)
print(result)  # 输出：(15, 5, 50, 2.0)（元组形式）

# 解构赋值（解包）
sum_val, diff_val, product_val, quotient_val = calculate(10, 5)
print(f"和：{sum_val}, 差：{diff_val}, 积：{product_val}, 商：{quotient_val}")
# 输出：和：15, 差：5, 积：50, 商：2.0


def sum_numbers(*args):
    print(f"接收到的位置参数：{args}")  # args 是一个元组
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(f"总和：{result}")  # 输出：总和：15


def print_info(**kwargs):
    print(f"接收到的关键字参数：{kwargs}")  # kwargs 是一个字典
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=18, city="北京")
# 输出：
# 接收到的关键字参数：{'name': '张三', 'age': 18, 'city': '北京'}
# name: 张三
# age: 18
# city: 北京
print('\n\n\n\n\n')

def greet(name, age):
    print(f"你好，{name}！你今年 {age} 岁。")

# 方法1：直接传递
greet("李四", 20)  # 输出：你好，李四！你今年 20 岁。

# 方法2：使用元组解包
info = ("王五", 22)
greet(*info)  # 相当于 greet("王五", 22)，输出：你好，王五！你今年 22 岁。

# 方法3：使用列表解包
info_list = ["赵六", 24]
greet(*info_list)  # 相当于 greet("赵六", 24)，输出：你好，赵六！你今年 24 岁。

def describe_person(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 方法1：直接传递
describe_person(name="小明", age=19, city="上海")  # 输出：姓名：小明，年龄：19，城市：上海
# 方法2：使用字典解包
person_dict = {"name": "小红", "age": 21, "city": "广州"}
describe_person(**person_dict)  # 相当于 describe_person(name="小红", age=21, city="广州")


def wrapper_func(*args, **kwargs):
    print(f"打包的位置参数：{args}")
    print(f"打包的关键字参数：{kwargs}")
    # 将打包的参数解包后传递给目标函数
    return target_func(*args, **kwargs)

def target_func(a, b, c=0, d=0):
    return a + b + c + d

# 调用示例
result = wrapper_func(1, 2, c=3, d=4)
print(f"结果：{result}")  # 输出：10