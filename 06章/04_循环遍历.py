scoreList = [12, 76, 97, 35, 65, 43]

# while 循环
index = 0
while index < len(scoreList):
    print(scoreList[index])
    index += 1

# for 循环
print('=============写法一==================')
for item in scoreList:
    print(item)


print('=============写法二==================')
for index in range(len(scoreList)):
    print(scoreList[index])


print('=============写法三==================')
for index, item in enumerate(scoreList):
    print(f'索引{index}, 每一项元素{item}')
