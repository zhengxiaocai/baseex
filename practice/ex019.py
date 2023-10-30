from itertools import groupby


def look_and_say(data='1', max_len=5):
    curr, res = data, []
    for _ in range(max_len):
        curr = ''.join(f'{len(list(g))}{c}' for c, g in groupby(curr))
        res.append(curr)
    return res


if __name__ == '__main__':
    expected = ['11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221',
                '13211311123113112211', '11131221133112132113212221']
    result = look_and_say('1', 10)
    print(result == expected)

    expected = ['111312', '31131112', '1321133112', '11131221232112', '31131122111213122112',
                '13211321223112111311222112', '1113122113121122132112311321322112',
                '311311222113111221221113122112132113121113222112']
    result = look_and_say('132', 8)
    print(result == expected)
