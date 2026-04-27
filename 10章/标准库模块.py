import os
import math
import random
import datetime
import json
print(os.__file__)
# os 模块
# os.mkdir("data")
print(f"当前目录：{os.getcwd()}")

# math 模块
print(f"π 的值：{math.pi}")
print(f"2 的平方根：{math.sqrt(2)}")

# random 模块
print(f"随机整数（1-10）：{random.randint(1, 10)}")

# datetime 模块
now = datetime.datetime.now()
print(f"当前时间：{now}")

# json 模块
data = {"name": "Alice", "age": 18}
json_str = json.dumps(data)
print(f"JSON 字符串：{json_str}")