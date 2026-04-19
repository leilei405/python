# 导入 reduce 函数（Python 3 中需要从 functools 模块导入）
from functools import reduce

# map：对可迭代对象中的每个元素应用函数
print(f'\n\n{"=" * 20}map{"=" * 20}')
result1 = list(map(lambda x: x * 2, range(10)))
print('map', result1)  # 输出：map [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# filter：过滤可迭代对象中的元素，保留符合条件的元素
print(f'\n\n{"=" * 20}filter{"=" * 20}')
result2 = list(filter(lambda x: x % 2 == 0, range(10)))
print('filter', result2)  # 输出：filter [0, 2, 4, 6, 8]

# sorted：对可迭代对象进行排序（默认升序）
print(f'\n\n{"=" * 20}sorted{"=" * 20}')
# 示例1：基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result3 = sorted(numbers)
print('sorted（默认升序）', result3)  # 输出：sorted（默认升序） [1, 1, 2, 3, 4, 5, 6, 9]

# 示例2：降序排序
result4 = sorted(numbers, reverse=True)
print('sorted（降序）', result4)  # 输出：sorted（降序） [9, 6, 5, 4, 3, 2, 1, 1]

# 示例3：自定义排序规则（例如按绝对值排序）
abs_numbers = [-3, 1, -4, 1, -5, 9, 2, -6]
result5 = sorted(abs_numbers, key=lambda x: abs(x))
print('sorted（按绝对值排序）', result5)  # 输出：sorted（按绝对值排序） [1, 1, 2, -3, -4, -5, 9, -6]

# reduce：对可迭代对象中的元素进行累积计算
print(f'\n\n{"=" * 20}reduce{"=" * 20}')
# 示例1：计算列表元素的和
sum_result = reduce(lambda x, y: x + y, range(1, 6))  # 1+2+3+4+5
print('reduce（求和）', sum_result)  # 输出：reduce（求和） 15

# 示例2：计算列表元素的乘积
product_result = reduce(lambda x, y: x * y, range(1, 6))  # 1*2*3*4*5
print('reduce（求积）', product_result)  # 输出：reduce（求积） 120