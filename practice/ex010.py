"""
给到一个字符串，判断字母A-Z是否在字符串中都至少出现过一次，忽略大小写。
"""


def is_pangram(s):
    return len(set([i.lower() for i in s if i.isalpha()])) == 26


if __name__ == '__main__':
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram(pangram) == True)
    
    
