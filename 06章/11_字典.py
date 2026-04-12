# 定义字典
# 注意：出现重复的key值 后面会将前面的覆盖掉
from linecache import updatecache

obj1 = {'age': 1, 'name': 'll', 'sex': 'man'}
obj2 = dict()
print('字典', obj1.get('name', '2222'))
print('空字典', obj2)

# 定义嵌套字典：外层字典的键为学生ID，值为包含学生信息的字典
students = {
    "s001": {
        "name": "张三",
        "age": 18,
        "grades": {  # 嵌套的成绩字典
            "语文": 92,
            "数学": 88,
            "英语": 95
        },
        "hobbies": ["篮球", "编程"]  # 嵌套的列表
    },
    "s002": {
        "name": "李四",
        "age": 17,
        "grades": {
            "语文": 85,
            "数学": 90,
            "英语": 82
        },
        "hobbies": ["绘画", "音乐"]
    }
}

# 访问嵌套字典的元素
print("\n\n张三的数学成绩:", students["s001"]["grades"]["数学"])  # 输出：88
print("李四的爱好:", students["s002"]["hobbies"])  # 输出：['绘画', '音乐']

# 修改嵌套字典的元素
students["s001"]["age"] = 19  # 更新张三的年龄
print("更新后张三的年龄:", students["s001"]["age"])  # 输出：19

# 批量修改
up = {'张三': '111', '李四': '2222'}
up.update({'张三': '333', '李四': '444'})
print('批量修改', up)
del up['张三']
print('删除对应键值对 del', up)
# pop 存在默认值，
# 无默认值：存在正常返回对应的值，不存在报错，
# 有默认值：存在正常返回对应的值，不存在返回默认值
ee = up.pop('李四')
print('删除对应键值对 pop', ee) # 444

# 添加新的嵌套键值对
students["s001"]["grades"]["物理"] = 90  # 给张三添加物理成绩
print("张三的物理成绩:", students["s001"]["grades"]["物理"])  # 输出：90

# 遍历嵌套字典
print("\n所有学生信息：")
for student_id, info in students.items():
    print(f"学生ID: {student_id}")
    print(f"  姓名: {info['name']}")
    print(f"  年龄: {info['age']}")
    print(f"  成绩: {info['grades']}")
    print(f"  爱好: {info['hobbies']}")