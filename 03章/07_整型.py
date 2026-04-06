# 所谓整型，就是没有小数点的数字，可以是正数，可以是负数，也可以是0
import sys

age = 18
temp = -12
score = 0

# 当数很大的时候，可以使用下划线将数字进行分组，更加易读
salary = 100_000_000
house_price = 3_200_000
graduates = 12_000_000

print(age, temp, score, salary, house_price, graduates)

# Python 中整数的上限值，取决于执行代码的计算机的内存和处理能力。
a = 9 ** 99999
sys.set_int_max_str_digits(0) # 0 表示不限制位数上限
print(a)