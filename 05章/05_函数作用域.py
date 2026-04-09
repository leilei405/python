print('=====================================示例 1：基本的全局与局部作用域======================================')
# 全局变量
global_var = "我是全局变量"

def test_scope():
    # 局部变量
    local_var = "我是局部变量"
    print("函数内部访问全局变量:", global_var)  # 可以读取全局变量
    print("函数内部访问局部变量:", local_var)  # 可以读取局部变量

test_scope()
print("函数外部访问全局变量:", global_var)  # 可以读取全局变量
# print("函数外部访问局部变量:", local_var)  # 报错：NameError，局部变量在外部不可访问

print('===================================示例 2：在函数内部修改全局变量（需使用 global）========================')

global_count = 0
def modify_global():
    global global_count  # 声明要修改的是全局变量
    global_count += 10
    print("函数内部修改后的全局变量:", global_count)

modify_global()  # 输出：函数内部修改后的全局变量: 1
print("函数外部的全局变量:", global_count)  # 输出：函数外部的全局变量: 1


print('===================================示例 3：嵌套函数中的作用域（nonlocal 的使用）========================')
def outer_func():
    outer_var = "外层函数变量"  # 嵌套作用域变量

    def inner_func():
        nonlocal outer_var  # 声明要修改的是外层函数的变量
        outer_var = "修改后的外层函数变量"
        print("内层函数访问外层变量:", outer_var)

    inner_func()
    print("外层函数访问变量:", outer_var)  # 输出修改后的值
outer_func()
# 输出：
# 内层函数访问外层变量: 修改后的外层函数变量
# 外层函数访问变量: 修改后的外层函数变量

print('=====================================示例 4：LEGB 规则演示===========================================')

# 全局作用域
x = "全局变量"
def outer():
    # 嵌套作用域
    x = "外层函数变量"

    def inner():
        # 局部作用域
        x = "内层函数变量"
        print("内层函数中的 x:", x)  # 优先使用局部变量

    inner()
    print("外层函数中的 x:", x)  # 使用嵌套作用域变量
outer()
print("全局作用域中的 x:", x)  # 使用全局变量