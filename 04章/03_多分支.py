age = int(input("请输入你的年龄：\n"))

if age <= 10:
    print("幼儿")
elif age <= 18:
    print("你是青少年")
elif age <= 30:
    print("青年")
elif age <= 50:
    print("中年")
elif age <= 60:
    print("中老年")
else:
    print("老年人")