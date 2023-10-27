def expanded_form(num):
    """ 初版 """
    bar = []
    for index, i in enumerate(reversed(str(num))):
        if i != '0':
            bar.append(i + '0' * index)
    return ' + '.join([i for i in reversed(bar)])


def expanded_form_update(num):
    """ 更新，一行式 """
    return ' + '.join(f'{v}{"0" * (len(str(num)) - i - 1)}' for i, v in enumerate(str(num)) if v != '0')


if __name__ == '__main__':
    print(expanded_form(12) == '10 + 2')
    print(expanded_form(42) == '40 + 2')
    print(expanded_form(70304) == '70000 + 300 + 4')
