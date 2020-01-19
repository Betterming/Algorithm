# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        """
        1.输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
        idea: n & (n - 1)会去掉二进制n末尾的1，比如 1101 & 1100 = 1100， 1010 & 1001 = 1000，通过这个只需循环n中1的个数次

        """
        if n < 0:
            n = n & 0xffffffff

        cnt = 0
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt

    def test(self, n):
        print('----------')
        print('n', n)
        print('bin n', bin(n))
        print('count bin n', bin(n).count('1'))
        if n < 0:
            n = n & 0xffffffffffffffff
        print('-----')
        print('n', n)
        print('bin n', bin(n))
        print('count bin n', bin(n).count('1'))



if __name__ == '__main__':
    solution = Solution()
    res1 = solution.NumberOf1(-3)
    print("NumberOf1: ", res1)
    solution.test(-5)

