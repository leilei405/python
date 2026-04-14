class Person:
    # 初始化方法 给实例添加属性
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法 给实例添加行为
    # 实例方法 保存在类上 供实例调用
    def speak(self, msg):
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} message: {msg}")

    # 自定义方法 给实例添加行为
    # # 实例方法 保存在类上 供实例调用
    def run (self, distance):
        print(f'{self.name}跑了{distance}米')


# 创建实例
p1 = Person('张三', 18, '男')
p2 = Person('李四', 24, '男')

print('Person实例方法/属性', Person.__dict__)
print('P1实例方法/属性', p1.__dict__)
print('P2实例方法/属性', p2.__dict__)

print('\n===========实例调用方法================')
p1.speak('msg')
p2.run(200)

print('\n===========类调用实例方法---不推荐================')
# 类调用实例方法
Person.run(p1, 200)