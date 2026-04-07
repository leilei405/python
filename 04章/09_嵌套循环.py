# for day in range(1, 31):
#     print(f'📅第{day}天')
#     for group in range(1, 3):
#         print(f"这是第一组{group}仰卧起坐")
#     print(f"✅第{day}任务已完成！明天继续\n")
# print("一个月健身目标完成")

day = 1
group = 1
while day <= 30 :
    print(f'📅第{day}天')
    group = 1
    while group <= 3:
        print(f"这是第一组{group}仰卧起坐")
        group += 1
    print(f"✅第{day}天健身任务已完成！明天继续\n")
    day += 1
print("一个月健身目标完成")