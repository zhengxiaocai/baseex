from itertools import groupby


def doubles(s):
    """ 首次解法，每次循环把出现偶数次的字母去掉变为新的字符串，直到字符串不再变化为止 """
    while True:
        res = ''.join(i * (len(list(g)) % 2) for i, g in groupby(s))
        if res == s:
            break
        s = res
    return res


def doubles_update(s):
    """ 临时变量存储，符合条件的才存储，重复的把之前的删掉 """
    res = []
    for i in s:
        if res and res[-1] == i:
            res.pop()
        else:
            res.append(i)
    return ''.join(res)


if __name__ == '__main__':
    print(doubles('abbbzz') == 'ab')
    print(doubles('zzzzykkkd') == 'ykd')
    print(doubles('abbcccdddda') == 'aca')
    print(doubles('vvvvvoiiiiin') == 'voin')
    print(doubles('rrrmooomqqqqj') == 'rmomj')
    print(doubles('xxbnnnnnyaaaaam') == 'bnyam')
