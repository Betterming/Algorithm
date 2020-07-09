class Solution:
    def __init__(self):
        pass
    def threeSum(self, nums):
        """
        L15.给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        idea:  排序 + 双指针 + 重点是去重
        总体思路：固定第一个元素，后面的俩个元素使用双指针
        1.特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 []。
        2.对数组进行排序。
        3.遍历排序后数组：
            若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
            对于重复元素：跳过，避免出现重复解
            令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
                当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
                若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
                若和小于 00，说明 nums[L]nums[L] 太小，LL 右移

        :param nums:
        :return:
        """
        numsLen = len(nums)
        if not nums or numsLen < 3:
            return []
        res = []
        newNums = sorted(nums)

        if newNums[0] > 0 or newNums[numsLen-1] < 0:
            return res
        for i in range(numsLen-2):
            if newNums[i] > 0:
                break
            if i > 0 and newNums[i] == newNums[i-1]:  # 用于去第一个元素重
                continue

            left = i + 1
            right = numsLen - 1
            while left < right:
                result = newNums[left] + newNums[right] + newNums[i]
                if result == 0:
                    res.append([newNums[left], newNums[i], newNums[right]])

                    # 用于去后两个元素重
                    while left < right and newNums[left] == newNums[left + 1]:
                        left += 1
                    while left < right and newNums[right] == newNums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif result < 0:
                    left += 1
                else:
                    right -= 1
        return res

    def lengthOfLongestSubstring(self, s):
        """
        L3: 无重复字符的最长子串,给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        :param s:
        :return:
        """
        if not s:
            return 0

        sLen = len(s)
        if sLen <= 0:
            return 0

    def minWindow(self, s: str, t: str) -> str:
        """
        L76.给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return ""
        sLen, tLen = len(s), len(t)
        left = right = 0
        res = sLen
        matched = 0
        need = {}
        window = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        while right < sLen:
            c1 = s[right]






if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.lengthOfLongestSubstring(("abcabcbb")))


