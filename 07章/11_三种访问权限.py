class Person:
    def __init__(self, name, age, gender):
        # 公有属性：当前类、子类、类外部 都可以访问
        self.name = name

        # 受保护属性：self._age 单个下划线，当前类，子类中可以访问
        self._age = age

        # 私有属性：self.__gender 两个下划线 只能在当前类中访问
        self.__gender = gender

    def speak(self, msg):
        print(f"我叫：{self.name} 年龄：{self._age} 性别：{self.__gender} 想说的话是: {msg}")

class Student(Person):
    def talk(self):
        print(self.name, self._age, self.__gender)

p1 = Person('浏览', 18, '男')
s1 = Student('德华', 19, '女')

p1.speak('比心')
s1.speak('学生访问行不行')
# s1.talk() # 报错

print(p1.name)
print(p1._age)  # 强制 也能访问 但是不推荐
print(s1.name)

# Python 底层是通过重命名的方式完成私有化的
# print(s1.__gender) # 报错
