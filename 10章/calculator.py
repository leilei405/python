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