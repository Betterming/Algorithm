# -*- coding:utf-8 -*-

"""
对于数学问题，首先要从小数举例开始，然后找到规律，用dp比较多，或者一些操作技巧，比如搜索技巧
"""
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

    def jumpFloorII(self, number):
        """
        2. 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
        动态规划：f(1) = 1, f(n) = 2*f(n)
        :return: 
        """
        if number <= 0:
            return 0
        if number == 1:
            return 1
        f = 1
        for _ in range(number - 1):
            f = f * 2
        return f

    def rectCover(self, number):
        """
        3. 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法
        idea：dp法，f(n) = f(n-1) + f(n-2)
        :return:
        """
        if number <= 0:
            return 0
        if number <= 3:
            return number

        f1 = 1
        f2 = 2
        for _ in range(number - 2):
            f2, f1 = f2 + f1, f2

        return f2



if __name__ == '__main__':
    solution = Solution()
    res1 = solution.Fibonacci(5)
    print("Fibonacci: ", res1)

    res2 = solution.jumpFloorII(5)
    print("jumpFloorII:", res2)
