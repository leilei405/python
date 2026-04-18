# 定义一个通用的计算函数（高阶函数）
def calculate(func, a, b):
    """接收一个函数参数 func，以及两个操作数 a 和 b"""
    return func(a, b)

# 定义具体的计算函数
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# 调用高阶函数，传入不同的函数实现不同逻辑
result1 = calculate(add, 10, 5)
print(f"加法结果：{result1}")  # 输出：15

result2 = calculate(subtract, 10, 5)
print(f"减法结果：{result2}")  # 输出：5

result3 = calculate(multiply, 10, 5)
print(f"乘法结果：{result3}")  # 输出：50
print('\n\n函数作为返回值')

# 定义一个返回函数的高阶函数
def make_operation(operation):
    """根据输入的操作类型，返回对应的计算函数"""

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract


# 获取返回的函数并调用
add_func = make_operation("add")
print(f"10 + 5 = {add_func(10, 5)}")  # 输出：15

subtract_func = make_operation("subtract")
print(f"10 - 5 = {subtract_func(10, 5)}")  # 输出：5
print('\n\n结合内置高阶函数（ map 、 filter ）')

# 示例1：使用 map（将函数应用于可迭代对象的每个元素）
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))
print(f"平方结果：{squared_numbers}")  # 输出：[1, 4, 9, 16, 25]

# 示例2：使用 filter（过滤出满足条件的元素）
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(f"偶数：{even_numbers}")  # 输出：[2, 4]
print('\n\n高阶函数的实际应用（排序）')


# 定义一个根据指定键排序的高阶函数
def sort_by_key(key_func):
    def sorter(items):
        return sorted(items, key=key_func)
    return sorter

# 定义排序键函数
def get_age(person):
    return person["age"]

def get_name_length(person):
    return len(person["name"])

# 测试数据
people = [
    {"name": "张三", "age": 25},
    {"name": "李四", "age": 18},
    {"name": "王五", "age": 30}
]

# 获取按年龄排序的函数
sort_by_age = sort_by_key(get_age)
sorted_by_age = sort_by_age(people)
print("按年龄排序：", sorted_by_age)
# 输出：按年龄排序： [{'name': '李四', 'age': 18}, {'name': '张三', 'age': 25}, {'name': '王五', 'age': 30}]

# 获取按名字长度排序的函数
sort_by_name_length = sort_by_key(get_name_length)
sorted_by_name = sort_by_name_length(people)
print("按名字长度排序：", sorted_by_name)
# 输出：按名字长度排序： [{'name': '张三', 'age': 25}, {'name': '李四', 'age': 18}, {'name': '王五', 'age': 30}]