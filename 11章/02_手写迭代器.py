# ============================================
# 一、手动实现迭代器的核心要点
# 1. __iter__() 方法: 返回迭代器对象本身 (self)
# 2. __next__() 方法: 返回下一个元素, 没有时抛出 StopIteration
# ============================================

# ------------------------------
# 示例1: 手动实现一个计数器迭代器
# ------------------------------
class CounterIterator:
    """计数器迭代器: 从 start 开始, 每次递增 step, 到 end 结束"""

    def __init__(self, start=0, end=10, step=1):
        self.start = start  # 起始值
        self.end = end  # 结束值
        self.step = step  # 步长
        self.current = start  # 当前值(状态)

    def __iter__(self):
        """返回迭代器对象本身"""
        return self

    def __next__(self):
        """返回下一个元素, 没有时抛出 StopIteration"""
        if self.current < self.end:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration  # 迭代结束


# 使用计数器迭代器
print("=== 计数器迭代器 ===")
counter = CounterIterator(start=1, end=10, step=2)
for num in counter:
    print(num, end=" ")  # 1 3 5 7 9
print()


# ------------------------------
# 示例2: 手动实现一个列表迭代器
# ------------------------------
class ListIterator:
    """自定义列表迭代器"""

    def __init__(self, data):
        self.data = data  # 要迭代的数据
        self.index = 0  # 当前索引(状态)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# 使用列表迭代器
print("\n=== 列表迭代器 ===")
fruits = ["apple", "banana", "cherry", "date"]
fruit_iter = ListIterator(fruits)
for fruit in fruit_iter:
    print(fruit)


# ------------------------------
# 示例3: 手动实现一个斐波那契数列迭代器
# ------------------------------
class FibonacciIterator:
    """斐波那契数列迭代器"""

    def __init__(self, max_n):
        self.max_n = max_n  # 最大项数
        self.a, self.b = 0, 1  # 初始值
        self.count = 0  # 已生成的项数

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration


# 使用斐波那契迭代器
print("\n=== 斐波那契迭代器 ===")
fib = FibonacciIterator(10)
for num in fib:
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()


# ------------------------------
# 示例4: 手动实现一个倒序迭代器
# ------------------------------
class ReverseIterator:
    """倒序迭代器"""

    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # 从最后一个元素开始

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration


# 使用倒序迭代器
print("\n=== 倒序迭代器 ===")
numbers = [1, 2, 3, 4, 5]
rev_iter = ReverseIterator(numbers)
for num in rev_iter:
    print(num, end=" ")  # 5 4 3 2 1
print()

# ============================================
# 二、迭代器协议的底层机制
# ============================================
print("\n=== 手动模拟 for 循环 ===")
my_list = [10, 20, 30]
iterator = ListIterator(my_list)

# for 循环的本质就是:
# 1. 调用 iter() 获取迭代器
# 2. 循环调用 next() 获取元素
# 3. 捕获 StopIteration 异常结束循环
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

# ============================================
# 三、可迭代对象 vs 迭代器
# ============================================
print("\n=== 可迭代对象 vs 迭代器 ===")


# 可迭代对象: 实现了 __iter__() 方法, 返回迭代器
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        """返回一个新的迭代器对象"""
        return ListIterator(self.data)


# 使用可迭代对象
my_iterable = MyIterable([1, 2, 3])
# 每次 for 循环都会调用 __iter__() 获取新的迭代器
for num in my_iterable:
    print(num, end=" ")  # 1 2 3
print()

for num in my_iterable:  # 可以多次遍历
    print(num, end=" ")  # 1 2 3