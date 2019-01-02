# 1.hello world！
# 任何一个编程语言都要跟世界打声招呼，Python3.x是这样式的：
print('Hello world!')
# Hello world!
# 
# 2.获取用户输入
name = input()
# 这样，用户就可以输入了，程序会获取用户的输入储存在name变量中。如果觉得比较突兀，可以给用户一个提示：
name = input('Input your name:')
# 
# 3.定义方法，实例：“获取绝对值”
def absolute(arg):
    if arg >= 0:
        return arg
    else:
        return -arg
# 
# 4.方法调用
absolute(9)
# 9
absolute(-9)
# 9
# 
# 5.转义字符 \
# \n 表示换行符，\t 表示制表符。如果想输出'\'本身，就要输出'\\'。如果不想转义，就在字符串前边加'r'
print('\\\n\\')
# \
# \
print(r'\\\n\\')
# \\\n\\
# 
# 
# 6.除法
# / 精确除
print(10 / 3)
# 3.3333333333333335
# / 哪怕能整除，也是一个浮点型
print(9 / 3)
# 3.0
# // 取整除
print(10 // 3)
# 3
# % 取余除
print(10 % 3)
# 1
# 
# 7.字符串替换
print('Hello %s!'%'leon')
# Hello leon
# 用%替换的时候，本身就有%时，就用%转义
print('hello %s %%'%'leon')
# hello leon %
# format格式化
print('hello {0}.'.format('leon'))
