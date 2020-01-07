# -*- coding:utf-8 -*-
class Solution:
    """
    1. 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    这是一个斐波那契数列
    """
    def jumpFloor(self, number):
        # write code here
        if number < 0:
            return 0
        if number <= 3:
            return number
        return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)

    def jumpFloor2(self, number):
        # write code here
        if number < 0:
            return 0
        if number < 4:
            return number
        j1 = 1
        j2 = 2
        for _ in range(number-2):
            j2, j1 = j2 + j1, j2
        return j2


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.jumpFloor(5)
    print("jumpFloor: ", res1)
