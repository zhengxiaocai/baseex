def smallest_transform(num):
    """ 初版 """
    res, num = [], [int(i) for i in str(num)]
    for i in num:
        res.append(sum(abs(i - j) for j in num))
    return min(res)


def smallest_transform_update(num):
    """ 更新一版，一行式子 """
    return min(sum(abs(int(j) - int(i)) for i in str(num)) for j in str(num))


if __name__ == '__main__':
    print(smallest_transform(399) == 6)
    print(smallest_transform(1234) == 4)
    print(smallest_transform(153) == 4)
    print(smallest_transform(33338) == 5)
    print(smallest_transform(7777) == 0)
    print(smallest_transform(977) == 2)
    print(smallest_transform(589) == 4)
