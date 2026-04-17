from datetime import datetime

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

    # 添加学生
    def add_student(self):
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        gender = input('请输入学生性别：')
        stu_info = Student(name, age, gender)
        self.stu_list.append(stu_info)
        print(f'✅添加成功！！！')

    # 删除学生
    def remove_student(self):
        sid = input('请输入学号：')
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
        if target:
            self.stu_list.remove(target)
            print('删除成功')
        else:
            print('学号不存在，删除失败，请重试！！！')

    # 查看所学生
    def show_students(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('没有学生！！！')

    # 设置学生成绩
    def set_score(self):
        sid = input('请输入学号：')
        for stu in self.stu_list:
            if stu.stu_id == sid:
                score_str = input('请输入成绩：(学科-学分，学科-学分)')
                score_list = score_str.replace('，', ',').split(',')
                for item in score_list:
                    subject, score = item.split('-')
                    subject = subject.strip()
                    score = float(score.strip())
                    stu.add_score(subject, score)
                print('添加成功！！！')
                return


    def run(self):
        while True:
            print('*************************************学生管理***********************************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            chocie = input('请输入操作编码')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.remove_student()
            elif chocie == '3':
                self.show_students()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('退出成功！！！')
                break
            else:
                print('输入有误！！！请重新输入')

m1 = Manager()
m1.run()
# s1 = Student('张三', 16, 'male')
# s2 = Student('李四', 16, 'male')
# s3 = Student('小明', 16, 'male')
# s1.add_score('数学', 80)
# s2.add_score('语文', 80)
# s3.add_score('英语', 80)
# print(s1)
# print(s2)
# print(s3)