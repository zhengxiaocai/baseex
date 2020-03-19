"""
https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python
编写一个函数toWeirdCase（weirdcase在Ruby中），该函数接受一个字符串，并返回相同的字符串，
每个单词中的所有偶数索引字符均大写，每个单词中的所有奇数索引字符均小写。
刚刚说明的索引是从零开始的，因此第零个索引是偶数，因此该字符应大写。

传入的字符串将仅由字母字符和空格（' '）组成。仅当有多个单词时才出现空格。单词将用单个空格（' '）分隔。

给一句话，返回的时候，每个单词的偶数index变为大写，奇数变为小写
"""


def to_weird_case(s):
    return ' '.join([''.join([v.lower() if i % 2 else v.upper() for i, v in enumerate(word)]) for word in s.split()])


if __name__ == '__main__':
    print(to_weird_case('This') == 'ThIs')
    print(to_weird_case('is') == 'Is')
    print(to_weird_case('This is a test') == 'ThIs Is A TeSt')
    print(to_weird_case('Weird string case') == 'WeIrD StRiNg CaSe')



