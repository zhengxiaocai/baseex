# set

# 可以看做是dict的key的一个集合

list = [1,1,2,2,3,3]
set01 = set(list)
print(set01)

# 定义格式
# Example = set(list)

# 定义的示例
set01 = set(list)
print(set01)

# 用set.add()方法添加
set01.add(4)
print(set01)

# 用set.remove()删除
# set01.remove(5)
set01.remove(4)
print(set01)

# 遍历
for i in set01:
    print(i)

# 使用index访问会报错
# set01[1]
