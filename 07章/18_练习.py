from datetime import datetime

print('*************************************学生管理***********************************')
print('1. 添加学生')
print('2. 删除学生')
print('3. 查看所有学生')
print('4. 录入成绩')
print('5. 退出')


# 基础信息
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 学生信息
class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.stu_id = f"{datetime.now().year}{Student.count:03d}"
        self.scores = {}

    # 添加学生成绩
    def add_score(self, subject, score):
        self.scores[subject] = score


    # 计算平均分
    def calculate_score(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    def __str__(self):
        return f'{self.name}信息：, {self.age}, {self.gender} 成绩：{self.scores} 平均分：{self.calculate_score()}'



# 管理
class Manager:
    def __init__(self):
        self.stu_list = []

    def add_student(self):
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        gender = input('请输入学生性别：')
        stu_info = Student(name, age, gender)
        self.stu_list.append(stu_info)
        print(f'✅添加成功！！！')

    # def remove_student(self):


# s1 = Student('张三', 16, 'male')
# s2 = Student('李四', 16, 'male')
# s3 = Student('小明', 16, 'male')
# s1.add_score('数学', 80)
# s2.add_score('语文', 80)
# s3.add_score('英语', 80)
# print(s1)
# print(s2)
# print(s3)