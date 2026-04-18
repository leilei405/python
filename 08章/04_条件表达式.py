# 简单的数字比较
age = 18
status = "成年人" if age >= 18 else "未成年人"
print(status)  # 输出：成年人

# 字符串处理
score = 95
result = "优秀" if score >= 90 else "良好"
print(result, '\n')  # 输出：优秀


print('嵌套条件表达式')
# 嵌套条件表达式（不推荐过于复杂的嵌套，影响可读性）
score = 85
result = "优秀" if score >= 90 else ("良好" if score >= 80 else "及格")
print(result)  # 输出：良好

# 等价于以下 if-else 结构
if score >= 90:
    result = "优秀"
elif score >= 80:
    result = "良好"
else:
    result = "及格"


# 判断列表是否为空
def get_list_status(lst):
    return "非空" if lst else "空列表"

print(get_list_status([1, 2, 3]))  # 输出：非空
print(get_list_status([]))         # 输出：空列表


# 根据条件为变量赋值
x = 10
y = 20
max_value = x if x > y else y
print(f"较大的值：{max_value}")  # 输出：较大的值：20