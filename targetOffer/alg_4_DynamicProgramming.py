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

    def lengthOfLIS(self, nums):
        """
        L300 最长上升子序列，求长度
        idea：
        :param nums:
        :return:
        """
        if len(nums) < 1:
            return 0
        n_len = len(nums)
        dp = [1] * n_len
        dp[0] = 1

        res = 1
        for i in range(1, n_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

            res = max(res, dp[i])
        return res

    def knapsack(self, N, W, wts, vals):
        """
        背包问题：N个物品，要装进质量只用Wkg的背包中，每个物品的质量和价值为wts[i],vals[i]，求最大的价值数。
        idea： dp关键点需要找到状态和选择，选择用来构建状态转移方程。
        dp[i][j]: 表示前i个物品不超过质量为j的最大价值数，最后的结果就是求dp[N][W]
        选择：对于第i个物品，可以选择放与不放。当wts[i-1] > j时，该物品肯定不能放。当wts[i-1] <= j 时，可放可不放。
                不放，dp[i][j] = dp[i-1][j]。放 dp[i][j] = dp[i-1][j-wts[i-1]] + vals[i-1]
        说明：i表示第i个物品，i从1开始，对应的质量时wts[i-1],价值vals[i-1]。
        二维dp的初始化为dp[...][0] = dp[0][...] = 0
        :param N:
        :param W:
        :param wts:
        :param vals:
        :return:
        """
        if W <= 0 or N <= 0 or len(wts) <= 0 or len(vals) <= 0:
            return 0

        dp = [[0] * (W+1) for _ in range(N+1)]  # 二维数组构造，不能是[[0] *m] * n,这样会
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j < wts[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wts[i-1]]+vals[i-1])
        return dp[N][W]

    def canPartition(self, nums):
        """
        L416. 分割等和子集
        一个包含全是正整数的非空集合，是否能分成两个子集，使得两边和相等。
        idea：
        1. 问题转化为：有一个能装质量为sum/2的背包，N个物品，各物品质量为nums[i],问，是否存在一种方法使得将背包装满。
        2. 同样用dp[i][j]表示前i个物品恰好能装j 质量吗？是为true，否为false。即求dp[N][sum/2]
        则：当第i个物品的质量nums[i-1] > j时 dp[i][j] = dp[i-1][j]. 大于时，dp[i][j] = dp[i-1][j] | dp[i-1][i-nums[i-1]
        dp[i][j]的状态等于第i个物品不放的状态 并上 第i个物品放入的状态。
        dp[...][0] = True, dp[0][...] = False
        :param nums:
        :return:
        """
        n_len = len(nums)
        if n_len < 1:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        dp = [[False] * (s // 2 + 1) for _ in range(n_len + 1)]
        for i in range(n_len + 1):
            dp[i][0] = True

        for i in range(1, n_len + 1):
            for j in range(1, s // 2 + 1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[n_len][s // 2]

        # dp = [False] * (s // 2 + 1)
        # dp[0] = True
        # for i in range(1, n_len+1):
        #     for j in range(s // 2, 0, -1):
        #         if j >

    def change(self, amount, coins):
        """
        L518: 给定一个不同面额的硬币和一个总金额，求组合种类数，各种硬币个数无限
        idea：dp[i][j] 表示前i个面额组合成j面额种类数。
        选择：可以选择第i个面额来组成j面额。dp[i][j] = dp[i][j-nums[i-1]]
        不选择第i个面额来组成j面额。dp[i][j] = dp[i-1][j]
        :param amount:
        :param coins:
        :return:
        """
        c_len = len(coins)
        if amount < 0 or c_len <= 0:
            return 0
        dp = [[0] * (amount+1) for _ in range(c_len+1)]
        for i in range(c_len+1):
            dp[i][0] = 1
        for i in range(1, c_len+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[c_len][amount]

    def longestPalindromeSubseq(self, s):
        """
        L516 最长回文子序列
        idea：dp[i][j]表示在[i,j]范围的最长回文子序列
        当s[i] = s[j]时 dp[i][j] = dp[i+1][j-1] + 2
        当s[i] != s[j]时， i，j分别向内移动一格时取得最大回文子序列
        :param s:
        :return:
        """
        n = len(s)
        if n <= 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

    def longestCommonSubSequence(self, str1, str2):
        """
        LCS:最长公共子序列
        子序列问题基本都要用到dp，因为子序列枚举要指数级的，而dp是穷举+剪枝完美解决子序列问题
        dp[i][j]表示：对于 s1[1..i] 和 s2[1..j] ， 它们的 LCS ⻓度是 dp[i][j] 。
        base case，我们专门让索引为 0 的⾏和列表⽰空串， dp[0][..] 和 dp[..][0] 都应该 初始化为 0，这就是 base case。
        状态转移方程：
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        :param str1:
        :param str2:
        :return:
        """
        m, n = len(str1), len(str2)
        if m <= 0 or n <= 0:
            return 0
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    def minDistance(self, s1, s2):
        def dp(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i + 1
            if s1[i] == s2[j]:
                return dp(i-1, j-1)
            else:
                return min(
                    dp(i-1, j) + 1,
                    dp(i, j-1) + 1,
                    dp(i-1, j-1) + 1
                )
        return dp(len(s1)-1, len(s2)-1)

    def minDistance2(self, s1, s2):
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo
            if i == -1:
                return j+1
            if j == -1:
                return i + 1
            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(
                    dp(i-1, j) + 1,
                    dp(i, j-1) + 1,
                    dp(i-1, j-1) + 1
                )
            return memo[(i, j)]
        return dp(len(s1)-1, len(s2)-1)

    def minDistance3(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + 1,  # 替换
                        dp[i-1][j] + 1,    # 删除
                        dp[i][j-1] + 1     # 增加
                    )
        return dp[m][n]

    def superEggDrop(self, K, N):
        """
        N层楼，K个鸡蛋，现确定有一个层数F在[0, N]之间，使得在该层扔鸡蛋恰好没摔碎。问：在最坏情况下，至少扔多少次找到这个F。
        idea：dp[i][j] 表示有j层楼，i个鸡蛋，最坏情况，至少需要的次数
        选择：在1-j层中选择dp最少的那一层扔鸡蛋。那一层设为x则 dp[i][j] = max(dp[i][j-x], dp[i-1][x-1]) + 1, x在1-j之间。
        待解决。
        :param K:
        :param N:
        :return:
        """
        memo = dict()
        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            for i in range(1, n+1):
                res = min(
                    res,
                    max(dp(k, n-i), dp(k-1, i-1))+1
                )
            memo[(k, n)] = res
            return res
        return dp(K, N)





if __name__ == '__main__':
    solution = Solution()
    res1 = solution.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
    print("FindGreatestSumOfSubArray: ", res1)

    res2 = solution.lengthOfLIS([1,5,3,4,6,9,7,8])
    print("lengthOfLIS: ", res2)

    res3 = solution.knapsack(3, 4, [2, 1, 3], [4, 2, 3])
    print("knapsack: ", res3)

    res4 = solution.canPartition([2, 1, 5])
    print("canPartition: ", res4)

    res5 = solution.change(5, [2, 1, 5])
    print("change: ", res5)

    res6 = solution.longestPalindromeSubseq('bbbab')
    print('longestPalindromeSubseq: ', res6)

    res7 = solution.longestCommonSubSequence('abcde', 'ace')
    print("longestCommonSubSequence: ", res7)

    res8 = solution.superEggDrop(2, 100)
    print('superEggDrop: ', res8)

