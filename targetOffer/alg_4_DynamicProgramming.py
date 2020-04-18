# -*- coding:utf-8 -*-
"""
动态规划：将一个问题拆分成几个子问题，分别求出子问题的解就能得到大问题的解，其他信息不需要
1. dp三性：用来判断是否可以用dp来求解
    1)无后效性：要求出f(15)，只需要知道f(14),f(10),f(4)的值，而f(14),f(10),f(4)是如何算出来的，对之后的问题没有影响。
    如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响
    2)最优子结构：f(n)的定义就已经蕴含了“最优”
    3)能拆分成相同形式的子问题：比如：最大连续子向量问题能拆成以i（i从0到len(array-1)）下标结尾的最大连续子向量，它们中最大的就是结果
2. dp三连：用来设计dp求解方式
    1) 状态量：f(i)表示的含义，以i结尾的最大连续子结构，以i结尾的LIS(最长上升子序列)长度,i元钱所需最少钞票数，跳到第i阶台阶种类数
    2) 状态转移方程：f(i) = max(0, f(i-1)) + array[i], dp[i] = max{dp[j]}(0<= j < i) + 1
    3) 初始量: f(0) = array[0]
"""



class Solution:
    def FindGreatestSumOfSubArray(self, array):
        """
        30.在一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
        但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
        例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
        给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
        idea: dp动态规划，f(i) = max(0, f(i-1)) + array[i]
        :param array:
        :return:
        """
        if len(array) < 1:
            return
        result = array[0]
        array_len = len(array)
        dp = [0] * array_len
        dp[0] = array[0]
        for i in range(1, array_len):
            if dp[i-1] <= 0:
                dp[i] = array[i]
            else:
                dp[i] = dp[i-1] + array[i]
            if result < dp[i]:
                result = dp[i]
        return result



if __name__ == '__main__':
    solution = Solution()
    res1 = solution.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
    print("FindGreatestSumOfSubArray: ", res1)