# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        """
        11.输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
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

    def Power(self, base, exponent):
        """
        12. 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。保证base和exponent不同时为0
        idea: 方法一：递推（O(n)）： dp[1] = base, dp[n] = dp[n-1] * base, 求dp[exponent]
        方法二：快速幂法，比如3^11 = 3^1 * 3^2 * 3^8, 就是将一个数11拆成若干个2的幂数相加（11 = 1 + 2 + 8），而这些幂数可以根据前面的幂数快速得到
        temp *= temp 比如初始temp = 3, 那么可以根据11的二进制位数(log(n)))依次获得3^2, 3^4, 3^8
        :param base:
        :param exponent:
        :return:
        """
        if exponent == 0:
            return 1
        flag = 1
        if exponent < 0:
            exponent = -1 * exponent
            flag = 0

        # 下面运算可以根据exponent的二进制1所在位置获得temp的1，2，4，8，... [lon(n)]（向上取整比如[log11] = 4）
        temp = base
        result = 1
        while exponent:
            if exponent & 1:
                result *= temp
            temp *= temp
            exponent = exponent >> 1

        return  result if flag else 1.0 / result


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.NumberOf1(-3)
    print("NumberOf1: ", res1)
    solution.test(-5)

    res2 = solution.Power(3, 5)
    print("Power: ", res2)

