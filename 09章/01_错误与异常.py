# 异常示例1：除零错误
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误：{e}")  # 输出：除零错误：division by zero

# 异常示例2：索引错误
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e:
    print(f"索引错误：{e}")  # 输出：索引错误：list index out of range

# 异常示例3：类型错误
try:
    result = "10" + 5
except TypeError as e:
    print(f"类型错误：{e}")  # 输出：类型错误：can only concatenate str (not "int") to str

# 异常示例4：键错误
try:
    person = {"name": "Alice", "age": 18}
    print(person["gender"])
except KeyError as e:
    print(f"键错误：{e}")  # 输出：键错误：'gender'
