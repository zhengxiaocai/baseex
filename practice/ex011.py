"""
https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
给一个数字，请在每个奇数整数之前和之后返回带有中划线（'-'）的字符串，但不要以中划线开头或结尾。
例如：
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""


def dashatize(num):
    result = []
    if isinstance(num, int):
        n = str(abs(num))
        for i, v in enumerate(n):
            if i == len(n) - 1:
                result.append(n[i])
                continue
            if int(n[i]) % 2 == 0 and int(n[i+1]) % 2 == 0:
                result.append(n[i])
            else:
                result.append(n[i])
                result.append('-')
        return ''.join(result)
    else:
        return str(num)


def dashatize_best(num):
    try:
        return ''.join(['-{}-'.format(i) if int(i)%2!=0 else i for i in str(abs(num))]).replace('--', '-').strip('-')
    except:
        return str(num)


if __name__ == '__main__':

    print(dashatize_best(274) == "2-7-4")
    print(dashatize_best(5311) == "5-3-1-1")
    print(dashatize_best(86320) == "86-3-20")
    print(dashatize_best(974302) == "9-7-4-3-02")
    print(dashatize_best(None) == "None")
    print(dashatize_best(0) == "0")
    print(dashatize_best(-1) == "1")
    print(dashatize_best(-28369) == "28-3-6-9")

