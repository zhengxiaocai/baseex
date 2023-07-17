"""
题目：
给出一个数组, 如[786, 28400, 347, 7732, 8498], 现在需要将数组中的数字拼接起来,
如按顺序依次拼接为: 7862840034777328498, 数组中的数字拼接顺序可以任意。

编写程序,返回最大的可以拼接的数字,(以上面数字为例, 返回: 8498786773234728400)
"""

"""
解题思路：
想获取最大的数字，应该把最高位最大的数字放到最前边拼接，如果最高位相同，那就比较第二位的大小。
比如题目中的：347应该在28400前边；786应该在7732前边。
"""

"""
我的做法：
以上的排序方法可以通过对字符串的排序来做
然后，再把字符串拼接起来，然后，转换格式就可以了。
"""


def get_max_num(nums):
    nums = [str(num) for num in nums]
    nums = sorted(nums, reverse=True)
    str_nums = ''.join(nums)
    return int(str_nums)


# 最佳实践，一行解决问题
def get_max_num_better(nums):
    return int(''.join(sorted([str(num) for num in nums], reverse=True)))


# 用map替代列表生成式
def get_max_num_best(nums):
    return int(''.join(sorted(map(str, nums), reverse=True)))


if __name__ == '__main__':
    test_nums = [786, 28400, 347, 7732, 8498]
    print(get_max_num(test_nums))
    print(get_max_num_better(test_nums))
    print(get_max_num_best(test_nums))
