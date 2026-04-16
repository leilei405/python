# 定义类1：鸟
class Bird:
    def fly(self):
        print("鸟在天空飞翔")

# 定义类2：飞机（与 Bird 无继承关系）
class Airplane:
    def fly(self):  # 同样有 fly 方法
        print("飞机在天空飞行")

# 测试函数：不关心参数类型，只要有 fly 方法即可
def let_it_fly(flyable):
    flyable.fly()  # 调用 fly 方法，无论对象是什么类型

# 测试
bird = Bird()
airplane = Airplane()

let_it_fly(bird)  # 输出：鸟在天空飞翔
let_it_fly(airplane)  # 输出：飞机在天空飞行