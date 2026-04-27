# # 导入整个模块
# import module_name
#
# # 导入模块中的特定函数或变量
# from module_name import function_name, variable_name
#
# # 导入模块中的所有内容（不推荐，可能导致命名冲突）
# from module_name import *
#
# # 给模块起别名（避免模块名过长）
# import module_name as mn


# calculator.py
"""计算器模块：提供基本的数学运算功能"""

# 变量
PI = 3.1415926535

# 函数
def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算（处理除零错误）"""
    if b == 0:
        return "错误：除数不能为零"
    return a / b