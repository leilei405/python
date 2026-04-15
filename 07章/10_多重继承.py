# 多重继承 ：指一个类同时继承多个父类，从而拥有多个父类的属性和方法。
# 类比 ：就像孩子不仅继承爸爸的长相，也能继承妈妈的性格。
# 定义父类1：Father（模拟爸爸的属性和方法）
class Father:
    def __init__(self, monkey):
        self.monkey = monkey

    def wokering(self):
        print(f"爸爸赚了{self.monkey}元")  # 爸爸的行为


# 定义父类2：Mother（模拟妈妈的属性和方法）
class Mother:
    def __init__(self, temperament):
        self.temperament = temperament

    def cook(self):
        print(f"妈妈会做饭, 并且可{self.temperament}了")  # 妈妈的行为


# 定义子类：Child（同时继承 Father 和 Mother）
class Child(Father, Mother):
    def __init__(self, monkey, temperament):
        # 调用两个父类的初始化方法（若父类有参数需传递）
        Father.__init__(self, monkey)
        Mother.__init__(self, temperament)
        self.name = "小明"  # 子类自身的属性


# 创建子类实例
child = Child('20000', '温柔')

# 访问父类1的属性和方法
child.wokering()

# 访问父类2的属性和方法
child.cook()

# 记录属性和方法的查找顺序  object 是所有类的父类
print(Child.__mro__) #  (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)