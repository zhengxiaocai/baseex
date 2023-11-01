def number_format(n):
    """ 格式字符串语法，还是值得学一下的 """
    return f'{n:,}'


if __name__ == '__main__':
    print(number_format(100000) == "100,000")
    print(number_format(5678545) == "5,678,545")
    print(number_format(-420902) == "-420,902")
    print(number_format(-3) == "-3")
    print(number_format(-1003) == "-1,003")
