class Person:
    # max_age、planet 都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 常用于保存公共数据
    max_age = 120
    planet = '嘿嘿哈哈'

    # 初始化方法
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.gender = gender
        if age < Person.max_age:
            self.age = age
        else:
            print('年龄超出最大范围', Person.max_age)
            self.age = Person.max_age


# 类属性保存在类身上的
print(Person.__dict__)
print(Person.max_age)
print(Person.planet)

# 实例上没有类属性
p1 = Person('张三', 1200, '男')
p2 = Person('李四', 24, '男')
print(p1.__dict__)
print(p2.__dict__)

print(Person.max_age)
print(p1.planet) # 先从自身查找  找不到再向上查找
print(p2.max_age)
