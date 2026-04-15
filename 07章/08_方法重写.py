class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} message: {msg}")

# 方法重写：如果子类中定义了跟父类同样的方法，那么子类中的方法会覆盖父类的方法
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    def speak(self, msg):
        super().speak(msg)  # 父类中的 speak 方法
        print(f"姓名：{self.name} 年龄：{self.age} 性别：{self.gender} 学号: {self.stu_id} 年级: {self.grade} 想说的话: {msg}")


s1 = Student('李华', 18, '男', '12222', '小初一')
s1.speak('你好坏，我好喜欢')