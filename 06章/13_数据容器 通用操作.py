print('=====================列表=======================')
# 定义空列表
empty_list = list()
print('定义空列表', empty_list, type(empty_list))  # []
# 将可迭代对象（如字符串）转换为列表
str_to_list = list("hello")
print('将可迭代对象（如字符串）转换为列表', str_to_list, type(str_to_list))  # ['h', 'e', 'l', 'l', 'o']
# 将元组转换为列表
tuple_to_list = list((1, 2, 3))
print('将元组转换为列表', tuple_to_list, type(tuple_to_list))  # [1, 2, 3]
# 将字典转换为列表
dict_to_list = list({ "age": '111', "name": '222' })
print("将字典转换为列表", dict_to_list, type(dict_to_list))


print('\n\n=====================元祖=======================')
# 定义空元组
empty_tuple = tuple()
print('定义空元组', empty_tuple, type(empty_tuple))   # ()
# 将可迭代对象（如列表）转换为元组
list_to_tuple = tuple([10, 20, 30])
print('将可迭代对象（如列表）转换为元组', list_to_tuple, type(list_to_tuple))  # (10, 20, 30)
# 将字符串转换为元组
str_to_tuple = tuple("test")
print('将字符串转换为元组', str_to_tuple, type(str_to_tuple))  # ('t', 'e', 's', 't')


print('\n\n=====================集合=======================')
# 定义空集合
empty_set = set()
print('定义空集合', empty_set, type(empty_set))  # set()
# 将可迭代对象（如列表）转换为集合（自动去重）
list_to_set = set([1, 2, 2, 3, 4])
print('将可迭代对象（如列表）转换为集合（自动去重）', list_to_set, type(list_to_set))  # {1, 2, 3, 4}
# 将元组转换为集合
tuple_to_set = set((10, 20, 30))
print('将元组转换为集合', tuple_to_set, type(tuple_to_set))  # {10, 20, 30}


print('\n\n=====================str=======================')
# 定义空字符串
empty_str = str()
print('定义空字符串', empty_str, type(empty_str))   # ""
# 将数字转换为字符串
num_to_str = str(123)
print('将数字转换为字符串', num_to_str, type(num_to_str))  # "123"
# 将列表转换为字符串
list_to_str = str([1, 2, 3])
print('将列表转换为字符串', list_to_str, type(list_to_str))  # "[1, 2, 3]"


print('\n\n=====================字典=======================')
# 定义空字典
empty_dict = dict()
print('定义空字典', empty_dict, type(empty_dict))   # {}
# 将包含键值对的可迭代对象（如列表）转换为字典
list_to_dict = dict([("name", "张三"), ("age", 18)])
print('将包含键值对的可迭代对象（如列表）转换为字典', list_to_dict, type(list_to_dict))  # {'name': '张三', 'age': 18}
# 将关键字参数转换为字典
kw_to_dict = dict(name="李四", age=19)
print('将关键字参数转换为字典', kw_to_dict, type(kw_to_dict))  # {'name': '李四', 'age': 19}


print('\n\n=====================not in / not=======================')
# 列表
my_list = [1, 2, 3, 4]
print(2 in my_list)  # True
print(5 not in my_list)  # True
# 元组
my_tuple = (10, 20, 30)
print(20 in my_tuple)  # True
print(40 not in my_tuple)  # True
# 集合
my_set = {100, 200, 300}
print(200 in my_set)  # True
print(400 not in my_set)  # True
# 字典（判断键是否存在）
my_dict = {"name": "张三", "age": 18}
print("name" in my_dict)  # True
print("gender" not in my_dict)  # True