strLearn = 'huanyingni，leileiccc'

# 获取索引
result1 = strLearn.index('a')

# 分割为字符串
result2 = strLearn.split(',')

# 出现次数
result3 = strLearn.count('c')

# 替换指定字符
result4 = strLearn.replace('a', 'A')

# strip 从某个字符串中删除指定字符串中的任意字符
# 会从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
result5 = strLearn.strip('cuh')

print(result1, result2, result3, result4)

print('死亡名单', result5)