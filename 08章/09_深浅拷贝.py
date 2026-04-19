import copy

# 原对象（包含嵌套的可变对象）
original = {
    "name": "Alice",
    "age": 20,
    "scores": [85, 90, 95]  # 嵌套列表（可变）
}

# 1. 赋值操作
assigned = original
print("赋值操作：")
original["age"] = 21
original["scores"][0] = 90
print(f"原对象：{original}")  # {'name': 'Alice', 'age': 21, 'scores': [90, 90, 95]}
print(f"赋值对象：{assigned}")  # {'name': 'Alice', 'age': 21, 'scores': [90, 90, 95]}（受影响）

# 2. 浅拷贝
original = {"name": "Alice", "age": 20, "scores": [85, 90, 95]}  # 重置原对象
shallow_copied = copy.copy(original)
print("\n浅拷贝：")
original["age"] = 21
original["scores"][0] = 90
print(f"原对象：{original}")  # {'name': 'Alice', 'age': 21, 'scores': [90, 90, 95]}
print(f"浅拷贝对象：{shallow_copied}")  # {'name': 'Alice', 'age': 20, 'scores': [90, 90, 95]}（嵌套元素受影响）

# 3. 深拷贝
original = {"name": "Alice", "age": 20, "scores": [85, 90, 95]}  # 重置原对象
deep_copied = copy.deepcopy(original)
print("\n深拷贝：")
original["age"] = 21
original["scores"][0] = 90
print(f"原对象：{original}")  # {'name': 'Alice', 'age': 21, 'scores': [90, 90, 95]}
print(f"深拷贝对象：{deep_copied}")  # {'name': 'Alice', 'age': 20, 'scores': [85, 90, 95]}（完全不受影响）

# 1.浅拷贝 会创建一个新对象， 但只拷贝原对象的顶层元素 。
# 2.对于嵌套的可变对象，浅拷贝仅复制其引用（即指向同一个嵌套对象）。
# 3.列表： list.copy() 、 new_list = original_list[:]
# 4.字典： dict.copy()
# 5.通用： copy.copy() （需要导入copy模块）


# - 深拷贝会创建一个新对象，并递归拷贝原对象的所有嵌套元素 （包括嵌套的可变对象）。修改原对象不会影响深拷贝后的对象。
# - 通用： copy.deepcopy() （需要导入copy模块）


