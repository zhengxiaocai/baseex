"""
超市里在排队结账，您的任务是编写一个函数，计算所有客户结账所需的时间！

输入：
customers：代表队列的正整数数组。每个整数代表一个客户，其值就是他们需要结帐的时间。
n：一个正整数，代表收银台的个数。

输出：
该函数应返回一个整数，即所需的总时间。

实例：
queue_time([5,3,4], 1) --> 12
解释：一个收银台的时候，只能挨个来，就是5+3+4=12
queue_time([2,3,10], 2) --> 12
解释：两个收银台，一个2，另一个是3，那最后一个10就会在第一个收银台，所以结果是12
queue_time([10,2,3,3], 2) --> 10
解释：两个收银台，一个是10，另一个是2+3+3，所以最后的结果是10
"""


def queue_time(customers, n):
        result = [0] * n
        for i in customers:
            result = sorted(result)
            result[0] += i
        return max(result)


if __name__ == '__main__':
    print(queue_time([5, 3, 4], 1) == 12)
    print(queue_time([10, 2, 3, 3], 2) == 10)
    print(queue_time([2, 3, 10], 2) == 12)
    print(queue_time([], 1) == 0)
    print(queue_time([5], 1) == 5)
    print(queue_time([2], 5) == 2)
    print(queue_time([1, 2, 3, 4, 5], 1) == 15)
    print(queue_time([1, 2, 3, 4, 5], 100) == 5)
    print(queue_time([2, 2, 3, 3, 4, 4], 2) == 9)
