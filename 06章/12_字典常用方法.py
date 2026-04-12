obj1 = {'张三': '99', '李四': '98'}

# keys 获取字典索引key
print('keys 获取索引key', obj1.keys())  # 返回[key1, key2]
print('类型', type(obj1.keys()))  # 类型: dict_keys

# dict_keys 与列表类似 但是不可以使用 下标
# 可以通过 list() 将其转换为 list

# values 获取所有的key对应的value 返回 [value1, value2]
print('获取所有的key对应的value', obj1.values())
print('类型', type(obj1.values()))
result = obj1.items()
print('获取所有的键值', result)

for key in obj1:
    print(key, obj1[key])

for key in obj1.keys():
    print(key, obj1[key])

