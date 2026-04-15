class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender

    # 注册age属性的getter方法 访问Person实例的age属性时候，age方法会被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性的setter方法 访问Person实例的age属性时候，age方法会被自动调用
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender not in ['男', '女']:
            print('性别错误')
        else:
            self.__gender = gender


p1 = Person('浏览', 18, '男')
p1.age = 20
p1.gender = '123'
print(p1.age)