list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 步长（n-1）位去取值，结束位置不算在内
# 起始位置：结束位置：步长
result = list1[0:5:1]
print('起始位置：结束位置：步长', result)

# 起始位置：结束位置：步长2
result2 = list1[2:7:2]
print('起始位置：结束位置：步长2', result2)

# 起始位置：结束位置：步长3
result3 = list1[1:8:3]
print('起始位置：结束位置：步长3', result3)

# result4 = list1[::] 等价于 list1[0:10:1]
result4 = list1[::]
print('list1[::] 等价于 list1[0:10:1]', result4)

# 结束位置999，没有那么多，会将列表长度做为索引值，不会报错
result5 = list1[:999:]
print('结束位置999，没有那么多，会将列表长度做为索引值，不会报错', result5)

# 当起始索引 大于 结束索引，步长必须为负数，否则结果是空列表
result6 = list1[11:3:-1]
print('当起始索引 大于 结束索引，步长必须为负数，否则结果是空列表', result6)

# 特殊情况，当同时省略起始索引和结束索引，步长为负数，那么Python会自动对调
result7 = list1[::-1]
print('特殊情况，当同时省略起始索引和结束索引，步长为负数，那么Python会自动对调', result7)


testList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('列表+列表', testList1 + testList2)
print('元祖+列元祖', tuple(testList1) + tuple(testList2))
print('字符串加字符串', type(str(testList1) + str(testList2)), str(testList1) + str(testList2))
print('列表相乘', testList1 * 3)
print('元祖相乘', tuple(testList1) * 3)
print('字符串相乘', str(testList1) * 3)

