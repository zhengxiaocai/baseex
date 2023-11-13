def changer(s):
    """ 小编解法，按需求一步步搞 """
    res = []
    for i in s:
        if i == 'z':
            res.append('a')
        elif i == 'Z':
            res.append('A')
        elif i.isalpha():
            res.append(chr(ord(i) + 1))
        else:
            res.append(i)
    res = [i.upper() if i.lower() in 'aeiou' else i.lower() for i in res]
    return ''.join(res)


def changer_update(s):
    """ 大佬，大道至简 """
    return s.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA'))


if __name__ == '__main__':
    print(changer('Cat30') == 'dbU30')
    print(changer('Alice') == 'bmjdf')
    print(changer('sponge1') == 'tqpOhf1')
    print(changer('Hello World') == 'Ifmmp xpsmE')
    print(changer('dogs') == 'Epht')
    print(changer('z') == 'A')
