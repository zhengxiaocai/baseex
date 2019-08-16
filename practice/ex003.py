
"""
今日份的题目：
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.    
意思就是：写一个波浪函数，比如我给你一个str，返回一个str的list，每一个str只有一个字母是大写，而且是从头到尾排列。可能描述起来比较费劲，看例子就知道了。
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
hello像一个波浪一样，从头浪到了尾。

def wave(str):
    # Code here

# testcase
result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("hello") == result)
​
result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
print(wave("codewars") == result)
​
result = []
print(wave("") == result)
​
result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave("two words") == result)
# 四个均为True，则通过。
"""


def wave(str):
    result = []
    for i in range(len(str)):
        if str[i] != ' ':
            if len(str)-1 > i:
                s = str[:i] + str[i].upper() + str[i+1:]
            else:
                s = str[:i] + str[i].upper()
        else:
            continue
        result.append(s)
    return result


# 优化后
def wave_good(str):
    result = []
    for i in range(len(str)):
        if str[i] != ' ':
            s = str[:i] + str[i].upper() + str[i+1:]
        else:
            continue
        result.append(s)
    return result


# 最佳
def wave_best(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i] !=' ']


if __name__ == '__main__':
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    print(wave("hello") == result)

    result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    print(wave("codewars") == result)

    result = []
    print(wave("") == result)

    result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    print(wave("two words") == result)

    result = []
    print(wave_good("") == result)

    result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    print(wave_good("two words") == result)

    result = []
    print(wave_best("") == result)

    result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    print(wave_best("two words") == result)


    # 测试空字符串和空格，作为条件
    if ' ':
        print('pass')
    else:
        print('fail')

    if '':
        print('Pass')
    else:
        print('Fail')


    # 测试截取的index
    s = 'Hello'
    print(s[5:4])


    """
    知识点：
    1. if ' ':
        print('空格会作为True条件')
    2. list[index1:index2]
        index1 index2 随便填，不会报错
    """



