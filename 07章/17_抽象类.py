from abc import ABC, abstractmethod

# 定义抽象类  继承了ABC  Animal 就是抽象类了
class Animal(ABC):
    @abstractmethod  # 标记为抽象方法
    def make_sound(self):
        """
            动物发出叫声的方法（子类必须实现）
        """
        pass  # 抽象方法没有具体实现

    @abstractmethod
    def move(self):
        """
            动物移动的方法（子类必须实现）
        """
        pass

    # 抽象类中也可以有普通方法（已有具体实现）
    def eat(self):
        print("动物需要吃东西")

# 定义子类1：狗（必须实现抽象方法）
class Dog(Animal):
    def make_sound(self):  # 实现抽象方法
        print("汪汪汪！")

    def move(self):  # 实现抽象方法
        print("狗在奔跑")

# 定义子类2：猫（必须实现抽象方法）
class Cat(Animal):
    def make_sound(self):  # 实现抽象方法
        print("喵喵喵！")

    def move(self):  # 实现抽象方法
        print("猫在跳跃")

# 测试
dog = Dog()
dog.make_sound()  # 输出：汪汪汪！
dog.move()        # 输出：狗在奔跑
dog.eat()         # 输出：动物需要吃东西

cat = Cat()
cat.make_sound()  # 输出：喵喵喵！
cat.move()        # 输出：猫在跳跃
cat.eat()         # 输出：动物需要吃东西

# 尝试直接实例化抽象类（会报错）
# animal = Animal()  # 报错：TypeError: Can't instantiate abstract class Animal with abstract methods make_sound, move