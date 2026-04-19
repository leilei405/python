# type()
print(type(10))  # <class 'int'>
print(type("hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# isinstance()
print(isinstance(10, int))  # True
print(isinstance("hello", str))  # True
print(isinstance([1, 2], list))  # True
print(isinstance(10, object))  # True（所有对象都是 object 的实例）

# issubclass()
print(issubclass(int, object))  # True
print(issubclass(list, object))  # True
class Animal:
    pass
class Dog(Animal):
    pass
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False

# id()
a = 10
b = 10
print(id(a))  # 140734667788176（示例值）
print(id(b))  # 140734667788176（小整数会被缓存，所以地址相同）
c = [1, 2, 3]
d = [1, 2, 3]
print(id(c))  # 不同的地址
print(id(d))  # 不同的地址


# 示例列表：l1 = [10, '2222', {}]
l1 = [10, '2222', {}]
print(all(l1))  # False（因为 {} 是假值）
print(any(l1))  # True（因为 10 和 '2222' 是真值）

# 其他示例
print(all([1, 2, 3]))  # True
print(all([1, 0, 3]))  # False（0 是假值）
print(all([]))  # True（空列表返回 True）

print(any([0, False, ""]))  # False（所有元素都是假值）
print(any([0, "hello", ""]))  # True（"hello" 是真值）
print(any([]))  # False（空列表返回 False）


# ord()
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48
print(ord('中'))  # 20013

# chr()
print(chr(65))  # 'A'
print(chr(97))  # 'a'
print(chr(48))  # '0'
print(chr(20013))  # '中'