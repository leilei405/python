class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} message: {msg}")

# Person 实例对象身上是没有speak方法的
p1 = Person('张三', 18, '男')
p2 = Person('李四', 24, '女')

# 所有Person类的实例对象，都可以调用到speak方法
# 当执行p1.speak() 的时候，查找speak方法的过程
#       1. 实例对象自身（p1）
#       2. 实例的缔造者身上 Person 父级去查找 逐级向上查找
p1.speak('你好啊')
p1.speak('我不好')


print('\n\n====================实例属性=================')
print('实例属性只能通过实例访问，不能通过类访问')
print('每个实例都有自己的实例属性，互不干扰')
