# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则: and会先看左边，如果左边是"假"，就直接返回左边，否则返回右边
# 备注: 若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(2 - 2 and True)
print('' and True)
print(True and 8 / 2)
print(3 + 3 and 3 * 4)


# or用于判断其两侧，是否至少有一个为True (只要有一个是True，那就返回True)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# or返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则: or会先看左边，如果左边是"真"，就直接返回左边，否则返回右边
# 备注: 若参与or运算的值不是布尔值，那or会自动转为布尔值，然后再进行逻辑操作


# not返回的值，一定是布尔值！
print(not 0)
print(not 3 > 2)
print(not 9 // 4)
print(not 'abc')