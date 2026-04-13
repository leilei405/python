# 定义一个类 Person
class Person:
    # 当一个函数被定义在了类中，那这个函数就被称为：方法
    # __init__方法：初始化方法，主要左右：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数: 当前正在创建的实例对象（self）、其它的自定义参数
    # 创建类实例的时，Python 会自动创建调用 __init__
    def __init__(self, name, age, gender):
        # 给实例添加属性（self.属性 = 值）
        self.name = name
        self.age = age
        self.gender = gender

print('\n\n====================创建类的实例对象=================')
p1 = Person('张三', 18, '男')
p2 = Person('李四', 24, '男')
p3 = Person('王麻子', 36, '女')

# 修改属性方法
p1.name = '王大头'

# 实例上追加属性
p2.address = '北京'

# type 追溯由哪个类创建出来的
print('type 追溯由哪个类创建出来的p1', type(p1))
print('type 追溯由哪个类创建出来的p2', type(p2))

print('P1 =', p1.name, p1.age, p1.gender, '所有属性值', p1.__dict__)
print('P2 =', p2.name, p2.age, p2.gender, '所有属性值', p2.__dict__)
print('P3 =', p3.name, p3.age, p3.gender, '所有属性值', p3.__dict__)