# 核心概念
# - object 类 是 Python 中所有类的顶层父类（基类）。
# - 任何在 Python 中定义的类，无论是否显式声明继承关系，都会 默认继承 object 类 。 为什么 object 是所有类的父类？
# - Python 的设计哲学是“万物皆对象”，而 object 类是所有对象的最基本类型。
# - 所有类继承自 object ，意味着它们会自动获得 object 类的内置方法（如 __str__ 、 __eq__ 等）。

# 显式继承 object（与默认行为一致）
class Person(object):
    pass

# 隐式继承 object（Python 3 中默认行为）
class Student:
    pass

# 验证继承关系
print(issubclass(Person, object))  # True
print(issubclass(Student, object))  # True

# 验证对象实例关系
p = Person()
s = Student()
print(isinstance(p, object))  # True
print(isinstance(s, object))  # True