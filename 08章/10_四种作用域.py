# Python函数进阶
# 局部作用域
def test():
    local_var = "我是局部变量"  # 局部作用域
    print(local_var)  # 函数内部可访问

test()  # 输出：我是局部变量
# print(local_var)  # 报错：NameError: name 'local_var' is not defined（外部无法访问）


# 外层作用域
def outer():
    outer_var = "我是外层变量"  # 外层作用域

    def inner():
        nonlocal outer_var

        # 只读访问外层变量
        print("内层函数访问外层变量：", outer_var) # 报错

        # 修改外层变量（需使用 nonlocal 声明）
        outer_var = "修改后的外层变量"
        print("修改后的外层变量：", outer_var)

    inner()
    print("外层函数访问变量：", outer_var)  # 外层变量被内层函数修改
outer()
# 输出：
# 内层函数访问外层变量： 我是外层变量
# 修改后的外层变量： 修改后的外层变量
# 外层函数访问变量： 修改后的外层变量


# 全局作用域
global_var = "我是全局变量"  # 全局作用域


def test():
    global global_var
    # 只读访问全局变量
    print("函数内部访问全局变量：", global_var)

    # 修改全局变量（需使用 global 声明）
    global_var = "修改后的全局变量"
    print("修改后的全局变量：", global_var)


test()
print("函数外部访问全局变量：", global_var)  # 全局变量被函数修改
# 输出：
# 函数内部访问全局变量： 我是全局变量
# 修改后的全局变量： 修改后的全局变量
# 函数外部访问全局变量： 修改后的全局变量



# 内建作用域
# 直接使用内建函数
print(len([1, 2, 3]))  # 输出：3（使用内建函数 len）
# 注意：若定义同名变量，会覆盖内建函数
len = 10  # 局部变量 len 覆盖内建函数
# print(len([1, 2, 3]))  # 报错：TypeError: 'int' object is not callable（此时 len 是整数，不是函数）