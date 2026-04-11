scoreList = []

while True:
    data = input('请输入成绩：')

    if data == '结束':
        print('结束输入')
        break
    else :
        scoreList.append(int(data))

if scoreList:
    # 统计平均分
    avgScore = sum(scoreList) / len(scoreList)
    # 合格人数
    passCount = 0
    # 优秀人数
    excellent = 0
    for score in scoreList:
        if score > 60:
            passCount += 1
        elif score > 90:
            excellent += 1
    # 合格率
    passRange = passCount / len(scoreList) * 100
    # 优秀率
    excelRange = excellent / len(scoreList) * 100

    print("🔽统计信息如下🔽")
    print(f'总人数{len(scoreList)}')
    print(f'最好成绩{max(scoreList)}')
    print(f'最差成绩{min(scoreList)}')
    print(f'合格率：{passRange}')
    print(f'优秀率：{excelRange}')
    print(f'优秀人数：{excellent}')
    print(f'合格人数：{passCount}')

else:
    print('您未输入成绩！！！')

# - 可存放不同类型的元素。
# - 元素是有序存储的（正索引、负索引）。
# - 列表中的元素允许重复。
# - 元素是允许修改的（增、删、改、查、其他操作）。
# - 长度不固定，可以随着操作自动调整大小。
