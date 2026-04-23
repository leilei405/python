# 变量类型注解
# 基本类型
age: int = 18
name: str = "Alice"
is_student: bool = True
price: float = 5.00


# 容器类型（需要从 typing 模块导入）
from typing import List, Dict, Tuple, Set

# 列表（元素类型为 int）
numbers: List[int] = [1, 2, 3, 4, 5]

# 字典（键类型为 str，值类型为 int）
scores1: Dict[str, int] = {"math": 90, "english": 85}

# 元组（固定长度和类型）
person: Tuple[str, int, bool] = ("Bob", 20, True)

# 集合（元素类型为 str）
fruits: Set[str] = {"apple", "banana", "cherry"}



def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

# 无返回值
def print_message(message: str) -> None:
    print(message)

from typing import List, Dict, Optional, Union, Callable

# 变量类型注解
user_id: int = 1001
username: str = "Bob"
is_active: bool = True
scores: Dict[str, int] = {"math": 90, "english": 85}
hobbies: List[str] = ["reading", "coding", "swimming"]
optional_value: Optional[str] = None
mixed_type: Union[int, str, bool] = 42

# 函数类型注解
def calculate_average(scores: List[int]) -> float:
    """计算平均分"""
    return sum(scores) / len(scores)

def process_data(data: Union[List[int], Dict[str, int]]) -> None:
    """处理数据（支持列表或字典）"""
    if isinstance(data, list):
        print(f"处理列表：{data}")
    elif isinstance(data, dict):
        print(f"处理字典：{data}")

# 函数类型变量
operation: Callable[[int, int], int] = lambda x, y: x * y

# 测试
print(calculate_average([85, 90, 95]))  # 90.0
process_data([1, 2, 3])  # 处理列表：[1, 2, 3]
process_data({"a": 1, "b": 2})  # 处理字典：{'a': 1, 'b': 2}
print(operation(5, 6))  # 30