from datetime import datetime

class Person:
    # 类属性
    max_age = 120
    planet = '嘿嘿哈哈'

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
    # 实例方法 保存在类上 供实例调用
    def run (self, distance):
        print(f'{self.name}跑了{distance}米')

    # 使用装饰器 @classmethod 装饰过的为 类方法
    # 类方法接收的参数 (cls 当前类本身, 其他参数)
    # 收到cls参数，类方法是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息，一些工厂方法
    @classmethod
    def talk(cls, msg):
        print(f'大声喧哗说出了{msg}', cls)
        cls.planet = msg

    # 使用装饰器 @classmethod 装饰过的为 类方法
    @classmethod
    def learn (cls, project):
        print(f'要开始学习了 卷死你们, 我要精通{project}')

    # 创建 类的工厂方法
    @classmethod
    def create(cls, info):
        # 获取Info 分割获取
        name, year, gender = info.split('-')
        # 获取当前年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - int(year)
        # 创建并返回一个Person的实力对象
        return cls(name, age, gender)

print(Person.__dict__)

# 类方法需要通过类调用
Person.talk('我喜欢你')

# 创建实例
p1 = Person('张三', 1200, '男')
p2 = Person('李四', 24, '男')

print('p1', p1.planet)
print('p2', p2.planet)

p3 = Person.create('小明-18-男')
print('p3', p3.__dict__)
