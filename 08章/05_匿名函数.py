# 定义一个计算平方的匿名函数
square = lambda x: x ** 2
print(square(5))  # 输出：25

# 定义一个计算两数之和的匿名函数
add = lambda a, b: a + b
print(add(3, 4))  # 输出：7



# 1. 与 map 配合：对列表中每个元素应用匿名函数
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, numbers)
print("用 for 循环遍历：")
for item in result:
    print(item, end=" ")  # 输出：1 4 9 16 25
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出：[1, 4, 9, 16, 25]

# 2. 与 filter 配合：过滤列表中的元素
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4]

# 3. 与 sorted 配合：自定义排序规则
students = [
    {"name": "张三", "score": 95},
    {"name": "李四", "score": 88},
    {"name": "王五", "score": 92}
]

# 按分数从高到低排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(sorted_students)
# 输出：[{'name': '张三', 'score': 95}, {'name': '王五', 'score': 92}, {'name': '李四', 'score': 88}]



# 作为函数参数
def calculate(func, a, b):
    return func(a, b)

# 传递匿名函数作为参数
result = calculate(lambda x, y: x * y, 10, 5)
print(result)  # 输出：50

# 作为函数返回值
def make_operation(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "subtract":
        return lambda x, y: x - y

add_func = make_operation("add")
print(add_func(10, 5))  # 输出：15