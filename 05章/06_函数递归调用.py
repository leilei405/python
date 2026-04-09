def test(n):
    print('num1', n)
    if n > 1:
        test(n - 1)

# test(5)

def test2(n):
    """
    求阶乘
    :param n: n的阶乘
    :return: 最终计算的值
    """
    if n == 0:
        return 1
    else:
        return n * test2(n - 1)

res = test2(10)
print(res)