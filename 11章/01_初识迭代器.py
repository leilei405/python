# ============================================
# 知识点1: 能被 for 循环遍历的对象, 被称为: 可迭代对象(iterable)
# ============================================
# 常见的可迭代对象: 列表、元组、字符串、集合、字典等
print("=== 可迭代对象示例 ===")
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
my_str = "hello"

# for 循环遍历
for num in my_list:
    print(num, end=" ")  # 1 2 3 4 5
print()

# ============================================
# 知识点2: 可迭代对象如何工作?
# 可迭代对象实现了 __iter__() 方法
# 通过 iter() 函数可以获取迭代器对象
# ============================================
print("\n=== 可迭代对象的本质 ===")
my_list = [1, 2, 3]
iterator = iter(my_list)  # 获取迭代器
print("迭代器对象:", iterator)  # <list_iterator object at 0x...>

# ============================================
# 知识点3: 迭代器(iterator)
# 迭代器实现了 __next__() 方法
# 通过 next() 函数逐个获取元素
# ============================================
print("\n=== 迭代器的工作原理 ===")
iterator = iter([1, 2, 3])

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration 异常


# ============================================
# 知识点4: for 循环的底层实现
# for 循环本质上是不断调用 next() 直到捕获 StopIteration
# ============================================
print("\n=== for 循环的本质 ===")
my_list = [1, 2, 3]
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

# ============================================
# 知识点5: 自定义迭代器
# 自定义类需要实现 __iter__() 和 __next__() 方法
# ============================================
print("\n=== 自定义迭代器 ===")


class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self  # 返回自身作为迭代器

    def __next__(self):
        if self.current < self.max_num:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # 结束迭代


# 使用自定义迭代器
for num in MyIterator(5):
    print(num, end=" ")  # 0 1 2 3 4
print()

# ============================================
# 知识点6: 迭代器的特点
# 1. 惰性计算: 只在需要时才生成下一个元素
# 2. 一次性: 迭代器只能遍历一次
# 3. 节省内存: 不需要一次性加载所有数据
# ============================================
print("\n=== 迭代器的特点 ===")
# 一次性遍历演示
numbers = iter([1, 2, 3])
print("第一次遍历:", list(numbers))  # [1, 2, 3]
print("第二次遍历:", list(numbers))  # [] (已经迭代完了)

# ============================================
# 知识点7: 生成器 - 简化的迭代器
# 使用 yield 关键字创建生成器
# ============================================
print("\n=== 生成器示例 ===")


def my_generator(n):
    for i in range(n):
        yield i  # 暂停执行,返回值给调用者


gen = my_generator(5)
print("生成器对象:", gen)  # <generator object my_generator at 0x...>

for num in gen:
    print(num, end=" ")  # 0 1 2 3 4
print()

# ============================================
# 知识点8: 常见的迭代器函数
# enumerate(), zip(), map(), filter() 等返回迭代器
# ============================================
print("\n=== 常用迭代器函数 ===")
# enumerate: 返回索引和元素
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# zip: 合并多个可迭代对象
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")