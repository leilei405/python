from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法 通过  @staticmethod 进行装饰  保存在类上
    # 单纯的定义在类中  不会收到 self cls 等参数， 收到的参数都是自定义参数
    # 由于静态方法没有收到 self cls 参数， 所以内部不会访问任何实例相关的内容
    # 静态方法通常用于定义一些工具方法
    @staticmethod
    def is_adult(year):
        return datetime.now().year - int(year) >= 18

    @staticmethod
    def is_equal(num1, num2):
        if num1 and num2:
            return int(num1) == int(num2)
        return False

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]

isAdult = Person.is_adult(2009)
isEqual = Person.is_equal(2, 2)
maskIdCard = Person.mask_idcard('6534287464536262525')

print(isAdult, isEqual, maskIdCard)