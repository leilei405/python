# main.py
import calculator
# 使用模块中的变量
print(f"圆周率：{calculator.PI}")
# 使用模块中的函数
print(f"3 + 5 = {calculator.add(3, 5)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")
print(f"6 * 7 = {calculator.multiply(6, 7)}")
print(f"8 / 2 = {calculator.divide(8, 2)}")
print(f"9 / 0 = {calculator.divide(9, 0)}")

