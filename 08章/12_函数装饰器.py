import time
import functools

# 示例1
# 定义装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        # 装饰器逻辑（在原函数执行前）
        # 调用原函数
        result = func(*args, **kwargs)
        # 装饰器逻辑（在原函数执行后）
        return result
    return wrapper

# 使用装饰器（语法糖）
@decorator
def target_function(x, y):
    return x + y

# print(target_function(1, 2))


# 示例2
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[日志] 开始执行函数：{func.__name__}")
        result = func(*args, **kwargs)
        print(f"[日志] 函数 {func.__name__} 执行完毕")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# 调用被装饰的函数
# result = add(3, 5)
# print(f"结果：{result}")

# [日志] 开始执行函数：add
# [日志] 函数 add 执行完毕
# 结果：8

# 示例3
def timer_decorator(unit="秒"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            if unit == "毫秒":
                duration *= 1000
            print(f"[计时] 函数 {func.__name__} 执行耗时：{duration:.2f} {unit}")
            return result
        return wrapper
    return decorator

@timer_decorator(unit="毫秒")
def slow_function():
    time.sleep(1)  # 模拟耗时操作
    print("函数执行完成")

# slow_function()


# 示例4
def my_decorator(func):
    @functools.wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        print("装饰器逻辑")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def original_function():
    """这是原函数的文档字符串"""
    print("原函数执行")

# 验证元信息是否保留
# print(f"函数名：{original_function.__name__}")
# print(f"文档字符串：{original_function.__doc__}")

# 示例5
def decorator1(func):
    print('装饰器1')
    def wrapper(*args, **kwargs):
        print("装饰器1：执行前")
        result = func(*args, **kwargs)
        print("装饰器1：执行后")
        return result
    return wrapper

def decorator2(func):
    print('装饰器2')
    def wrapper(*args, **kwargs):
        print("装饰器2：执行前")
        result = func(*args, **kwargs)
        print("装饰器2：执行后")
        return result
    return wrapper

# @decorator1
# @decorator2
def target():
    print("原函数执行")

# target()

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"函数 {self.func.__name__} 已被调用 {self.calls} 次")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # 输出：函数 greet 已被调用 1 次；Hello, Alice!
greet("Bob")  # 输出：函数 greet 已被调用 2 次；Hello, Bob!