"""
今日份的题目：
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

def high(x):
    # Code here
    
# testcase
print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
# 三个均为True，则通过。
"""


# 小编解法
def high(x):
    return sorted([i for i in x.split()], key=lambda y: sum(ord(j) - 96 for j in y), reverse=True)[0]


# 目前最佳解法
def high_best(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


if __name__ == '__main__':
    print(high('man i need a taxi up to ubud') == 'taxi')
    print(high('what time are we climbing up the volcano') == 'volcano')
    print(high('take me to semynak') == 'semynak')

"""
知识点：
1.获得字母的ASCII码值，ord()
    ord('a')
    >>>97
2.将一句话切割成一个列表，不需要列表生成式
    s = 'man i need a taxi up to ubud'
    li = [x for x in s.split()]
    >>>['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud']
    其实，s.split()已经完成工作了。
    s.split()
    >>>['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud']
3.max()方法也可以传key
    将一个匿名方法传进，形成规则。
4.如果存在多个最大的，max()默认返回第一个找到的
"""
