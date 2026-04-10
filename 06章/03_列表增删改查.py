addList = [1, 2, 3, 4, 5, 6]
# 末尾追加
# addList.append(6)
print('追加元素', addList)

# 指定索引 增加
addList.insert(2, 8)
print('指定索引 增加元素', addList)

# 将可迭代对象内容去除，追加到最后
addList.extend([7, 8, 9])
print('将可迭代对象内容去除，追加到最后', addList)

delList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
n = [2, 3]
print('删除元素', delList, n.clear())
