def reverse(a):
    """ 初版，根据原始list的元素长度去切片 """
    res = []
    s = ''.join(a)[::-1]
    for w in a:
        res.append(s[:len(w)])
        s = s[len(w):]
    return res


def reverse_update(a):
    """ 更新版本，利用迭代器的特性，嵌套循环去取 """
    s = reversed(''.join(a))
    return [''.join(next(s) for _ in w) for w in a]


if __name__ == '__main__':
    print(reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]) == ["!", "eilt", "onn", "acIdn", "ast",
                                                                                   "t", "ubgibe", "kilI"])
    print(reverse(
        ["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn",
         "amwoH"]) == ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts",
                       "to", "turn", "pink?"])
