# 最简单的判断
age = input()
if int(age)>18:
    print('成年人')

# 带and or not之类的复合判断
age = input()
if int(age)>18 and int(age)<30:
    print('最美好的年龄，好好珍惜')

# if - else
age = input()
if int(age) >= 18:
    print('成年人')
else:
    print('未成年')

# if - elif - else
age = input()
if int(age)<18:
    print('未成年')
elif int(age)<50:
    print('中年人')
else:
    print('老年人')
