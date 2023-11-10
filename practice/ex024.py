import re


def solve(eq):
    """ 初版，在str逆序之后，再把数字倒转过来 """
    res, curr = '', ''
    for i in eq[::-1]:
        if i not in '+-*/':
            curr += i
        else:
            res += curr[::-1]
            res += i
            curr = ''
    return res + curr[::-1]


def solve_better(eq):
    """ re.split(pattern, string) """
    return ''.join(reversed(re.split(r'(\W+)', eq)))


if __name__ == '__main__':
    print(solve("100*b/y") == "y/b*100")
    print(solve("a+b-c/d*30") == "30*d/c-b+a")
    print(solve("a*b/c+50") == "50+c/b*a")
