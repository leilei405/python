total = 0
svg = 0


def success():
    print(f"总数：{total}, 平均值{svg}")
    if total > 100:
        print("✅恭喜！挑战成功")


def main():
    print("【仰卧起坐】【7天】👊🏻挑战赛（请输入每天的数量）")
    global total
    global svg
    days = 1
    while days < 8:
        print(f"第{days}天", end=" ")

        total += int(input())
        days += 1
    svg = float(total / days)
    print("【仰卧起坐】【7天】健身总结")
    success()


main()
