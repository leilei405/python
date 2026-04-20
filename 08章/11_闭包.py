def outer():
    num = 10
    num += 1
    print(num)

# outer() # 11
# outer() # 11
# outer() # 11

# - 定义
#   - 当一个内层函数 引用了 外层函数 作用域中的变量，并且外层函数返回了这个内层函数时，就形成了闭包。即使外层函数执行完毕，内层函数仍然可以访问外层函数的变量。
# - 核心条件
#   - 嵌套函数 ：存在内层函数和外层函数的嵌套结构。
#   - 变量引用 ：内层函数引用了外层函数作用域中的变量。
#   - 函数返回 ：外层函数返回了内层函数
# - 工作原理
#   - 当外层函数执行时，会创建一个局部作用域，并在其中定义变量。
#   - 内层函数引用了外层函数的变量，形成了对该变量的“引用”。
#   - 当外层函数返回内层函数时，内层函数会“携带”外层函数的变量（即使外层函数的作用域已被销毁）。
# - 特点
#   - 变量持久化 ：外层函数的变量在函数执行完毕后不会被销毁，而是被内层函数“捕获”并继续使用。
#   - 独立性 ：不同的闭包实例（如 counter1 和 counter2 ）之间的变量是独立的，互不影响。
#   - 封装性 ：外层函数的变量对外部代码是隐藏的，只有内层函数可以访问，实现了数据的封装。
# - 应用场景
#   - 计数器 ：如示例1，用于跟踪状态（如点击次数、循环次数）。
#   - 配置参数 ：如示例2，根据不同参数创建不同功能的函数（如乘法器、格式化器）。
#   - 缓存 ：存储计算结果，避免重复计算（如斐波那契数列的缓存）。
#   - 装饰器 ：闭包是装饰器的核心实现机制。
# - 注意
#   - 内存管理 ：闭包会持有外层函数的变量，可能导致内存占用增加。如果闭包不再使用，应及时释放引用（如 counter = None ）。
#   - 可变对象 vs 不可变对象 ：
#     - 对于 可变对象 （如列表、字典），修改其内容无需 nonlocal 声明（因为引用未变）。
#     - 对于 不可变对象 （如数字、字符串），修改其值需使用 nonlocal 声明（因为需要重新赋值）。

def create_counter():
    count = 0  # 外层函数的局部变量

    def counter():
        nonlocal count  # 修改外层变量需要使用 nonlocal
        count += 1
        return count
    return counter  # 返回内层函数

# 创建两个计算器
counter1 = create_counter()
counter2 = create_counter()
# print('counter1() = ', counter1())
# print('counter1() = ', counter1())
# print('counter1() = ', counter1())
# print('counter2() = ', counter2())
# print('counter2() = ', counter2())

def make_multiplier(n):
    count = 0

    def multiplier(x):
        return x * n  # 引用外层函数的变量 n
    return multiplier

double_multiplier = make_multiplier(2)
triple_multiplier = make_multiplier(3)
# print(double_multiplier(3))
# print(triple_multiplier(5))

def track_history():
    history = []  # 外层函数的局部变量（列表、可变对象）

    def add_record(item):
        history.append(item)   # 修改可变对象，无需nonlocal
        return history.copy()  # 返回历史记录的副本

    return add_record

record = track_history()

print(record('step1'))  # ["step1"]
print(record('step2'))  # ["step1", "step2"]
print(record('step3'))  # ["step1", "step2", "step3"]