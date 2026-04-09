# args 接受可变位置参数
def test1(*args):
    print("args 接受可变位置参数，拿到的是元祖", args)

test1('lucky', 'test1', 'test2')

# kwargs 接受可变关键字参数，拿到的是字典
def test2(**kwargs):
    print("args 接受可变关键字参数，拿到的是字典", kwargs)

test2(age=18, name="lucky", sex="male")

# 同时使用可变位置参数、可变关键字参数
def test3(a, b, *args, c = 'default', **kwargs):
    print('==========================')
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

test3('lucky', 'test1', 'test2', 'test3', age = 18, height = 170)