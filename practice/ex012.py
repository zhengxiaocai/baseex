# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python


def reverse_words(text):
    return ' '.join([''.join(list(reversed(word))) for word in text.split(' ')])


def reverse_words_best(text):
    return ' '.join([word[::-1] for word in text.split(' ')])


if __name__ == '__main__':
    print(
        reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god')
    print(reverse_words('apple') == 'elppa')
    print(reverse_words('a b c d') == 'a b c d')
    print(reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow')
    print(reverse_words('  ab  ') == '  ba  ')
    print(reverse_words(' a b c  ') == ' a b c  ')
    
    # print('###'.split('#'))
    #
    # print('  ab  '.split())
    # print('  ab  '.split(' '))
    #
    # print(''.join(list(reversed('abc'))))
    # print('abc'[::-1])

    """
    知识点1：
    split()的用法，如果参数为空，就当作一个分隔符
    如果参数指定，就用指定的参数当分隔符
    
    知识点2：
    字符串反转
    ''.join(list(reversed('abc')))
    'abc'[::-1]
    """
