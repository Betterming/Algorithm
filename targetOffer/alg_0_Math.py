# -*- coding:utf-8 -*-
class Solution:
    """
    1. 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
    n<=39
    """
    def Fibonacci(self, n):
        # write code here
        f0 = 0
        f1 = 1
        if n < 2:
            return n
        for i in range(n):
            f1, f0 = f1 + f0, f1
        return f0


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.Fibonacci(5)
    print("Fibonacci: ", res1)
