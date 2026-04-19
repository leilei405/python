# 传统 for 循环 + append() 写法
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 列表推导式写法（简写）
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 传统 for 循环 + append() 写法
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
print(evens)  # [0, 2, 4, 6, 8]

# 列表推导式写法（带条件）
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


words = ["apple", "banana", "cherry"]

# 传统 for 循环 + append() 写法
capitalized = []
for word in words:
    capitalized.append(word.capitalize())
print(capitalized)  # ['Apple', 'Banana', 'Cherry']

# 列表推导式写法
capitalized = [word.capitalize() for word in words]
print(capitalized)  # ['Apple', 'Banana', 'Cherry']


# 传统 for 循环写法
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j)
    matrix.append(row)
print(matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 列表推导式写法（嵌套）
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]



def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

# 传统 for 循环 + append() 写法
doubled = []
for num in numbers:
    doubled.append(double(num))
print(doubled)  # [2, 4, 6, 8, 10]

# 列表推导式写法
doubled = [double(num) for num in numbers]
print(doubled)  # [2, 4, 6, 8, 10]