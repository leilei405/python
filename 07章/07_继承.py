class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} message: {msg}")

# 定义一个Student类 继承自Person
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 方式一 super() 直接复用父类中的属性 推荐
        super().__init__(name, age, gender)

        # 方式二 直接用 Person类
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性 需要自己手动初始化
        self.stu_id = stu_id
        self.grade = grade

    def speak(self, msg):
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} 学号: {self.stu_id} 年级: {self.grade} 想说的话: {msg}")
    # 略过
    # pass


# 创建 Student 实例对象
s1 = Student('李华', 18, '男', '12222', '小初一')
print(s1.__dict__)  # 李华
print(type(s1))  # <class '__main__.Student'>
s1.speak('都是')  #  先从实例自身找s1 => Student => 找不到再向父类Person找