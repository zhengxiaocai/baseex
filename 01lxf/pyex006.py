# for循环
# 语法结构
# for iter_var in iterable:
#     suite_to_repeat

# 循环访问list
classmates = ['Tom','Jerry','Curry']
for guys in classmates:
    print(guys+' ',end='')

# 字符串示例
word = 'Python'
for code in word:
    print(code+' ',end='')

# 迭代器结合，用来计数
for i in range(10):
    print('do ',end='')
