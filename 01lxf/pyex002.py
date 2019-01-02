# list 内置
classmates = ['Tom','Jerry','Curry']

# len
print(len(classmates))

# 取单个元素的值 0~len()-1
print(classmates[0], classmates[1], classmates[2])

# index超了 会报异常
# print(classmates[3])

# index还可以倒着数
print(classmates[2],classmates[-1])

# 列表元素添加：最后添加
classmates.append('Jordan')
print(classmates)

# 列表元素添加：指定位置
classmates.insert(1, 'James')
print(classmates)

# 弹出列表末尾元素，叫删除是不准确的，弹出
# 删掉列表最后一个元素，并且将它返回
print(classmates.pop())

# 弹出指定位置元素
print(classmates.pop(1))

# 更新，具体位置更新
print(classmates)
classmates[0] = 'Jack'
print(classmates)

# 强大的地儿，可以数据类型不一样
list = [1, 3.14, 'a', [1,2], True]

