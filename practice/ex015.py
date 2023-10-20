# https://www.codewars.com/kata/57f7796697d62fc93d0001b8


def trouble(x, t):
    """ 初版，外层是最大遍历次数，会有多遍历 """
    for _ in range(len(x)):
        for i in range(len(x) - 1):
            if x[i] + x[i + 1] == t:
                x.pop(i + 1)
                break
    return x


def trouble_better(x, t):
    """ 更新了一下，如果不再变化了，就提前跳出 """
    for _ in range(len(x) - 1):
        curr = len(x)
        for i in range(len(x) - 1):
            if x[i] + x[i + 1] == t:
                x.pop(i + 1)
                break
        if curr == len(x):
            break
    return x


def trouble_best(x, t):
    """ 不去删除，而是选择合适的增加 """
    res = []
    for i in x:
        if not res or res[-1] + i != t:
            res.append(i)
    return res


if __name__ == '__main__':
    print(trouble([1, 3, 5, 6, 7, 4, 3], 7) == [1, 3, 5, 6, 7, 4])
    print(trouble([4, 1, 1, 1, 4], 2) == [4, 1, 4])
    print(trouble([2, 6, 2], 8) == [2, 2])
    print(trouble([2, 2, 2, 2, 2, 2], 4) == [2])
