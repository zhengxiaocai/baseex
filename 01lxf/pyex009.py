# coding:utf-8

# dict get方法
newDict = {
    'name': 'Tom',
    'age': 19
}

# 做操作都是根据key做得操作
for key in newDict:
    print(key, newDict[key])

# 判断key是否存在用in方法
# 不存在返回False
print('job' in newDict)
# 存在返回True
print('name' in newDict)

# 判断key是否存在用get()方法
# 不存在返回None
print(newDict.get('job'))
# 存在返回key对应的value值
print(newDict.get('name'))
# 自己定制不存在的时候的返回信息
print(newDict.get('job','nojob'))

# 字典也可以用pop()删除，参数必传
# 正常传参数调用
newDict.pop('name')
# 参数不传会报语法错误
# newDict.pop()
