# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        """
        67.给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
        请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
        idea:
        1)k[0]到k[m]可能有哪些数字，实际上只可能是2或者3。当然也可能有4，但是4=2*2，可忽略。
            5<2*3,6<3*3,比6更大的数字我们就更不用考虑了，肯定要继续分。
        2)2和3的数量，一般2的数量要小于3个，因为2*2*2<3*3，但7=2*2*3。用贪心算法，要用尽可能多的3，所用
        直接用n除以3，根据得到的余数判断是一个2还是两个2还是没有2就行了。
        由于题目规定m>1，所以2只能是1*1，3只能是2*1，这两个特殊情况直接返回就行了。
        乘方运算的复杂度为：O(log n)，用动态规划来做会耗时比较多。
        :param number:
        :return:
        """
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        x = number % 3
        y = number / 3
        if x == 0:
            return int(pow(3, y))
        elif x == 1:
            return 4 * int(pow(3, y-1))
        else:
            return 2 * int(pow(3, y))
