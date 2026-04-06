# 自己定义的布尔值
a = True
b = False

# 靠程序执行得到的布尔值
c = 5 > 3
d = 7 < 2

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
print(int(True))
print(int(False))

# 使用bool 将内容转换为布尔类型
print(bool(111), 'bool1')
print(bool(000), 'bool2')
