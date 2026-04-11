print('=============正常传递参数==================')


def test1(data):
    print(f'参数：{data}')


list1 = [100, 200, 300, 400]
tuple1 = ('你好', '北京', '欢迎你')

# 正常传递参数
test1(list1)
test1(tuple1)

print('\n=============解包后传递参数==================')


def test2(*data):
    print(f'参数：{data}')

list2 = [100, 200, 300, 400]
tuple2 = ('你好', '北京', '欢迎你', '333')

test2(*list2)
test2(*tuple2)
