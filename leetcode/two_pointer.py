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
        idea：解题思路
        采用滑动窗口法
        - 首先，需要明确思路：s字符串维护一个窗口[left, right), right先一直移动直到窗口内部字符串全部包含T字符串为止，即找出可行解。此时left才开始移动直到不满足条件为止。
        - 其次，如何设计出满足窗口内字符串包含T的所有字符这一条件。
          - 针对T，S分别构造一个字典 need = defaultdict(int), window = defaultdict(int)。其中key为T/S中不重复的字符，value为其字符个数。
          - 构造一个变量matched，表示窗口内满足need条件的字符数，当matched == len(need)，表示窗口已经覆盖字符串T
        - 最后，怎样获得最小字串。设置res=MAX，start = 0，当matched == len(need)时，更新res，start。通过s[start: start:res]获取结果

        步骤：
        - 边界检查，初始化s长度sLen，res=sLen + 1，start=0；left = right = 0；matched = 0；window = defaultdict(int)，need = defaultdict(int)；获得need字典，need中value不为0的个数nLen
        - 滑动right：
          - 先获得c1 = s[right],然后right右移
          - 若c1在need中，更新window
            - 若c1在窗口中个数等于T中c1字符个数，则更新matched
          - 当matched等于need大小，即窗口已覆盖字符串T时，可以移动left了
            - 首先更新一波res，start。（最后结果肯定是在此状态下取得的。）
            - 然后先取得c2=s[left]，然后left右移
            - 最后判断c2是否在need中
              - 若在：(一定更新window，可能更新matched)
                - 判断window[c2]是否等于need[c2]
                  - 等于，则更新matched
                  - 不等于，不更新matched
                - 更新window
              - 若不在：window和matched都不用更新
        - 最后如果res没有改变过，则返回“”，改变过返回s[start: start:res]

链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/76-zui-xiao-fu-gai-zi-chuan-by-betterming-3/
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return ""

        sLen = len(s)
        left = right = 0
        res = sLen + 1
        matched = 0
        start = 0
        from collections import defaultdict
        window = defaultdict(int)
        need = defaultdict(int)

        for i in t:
            need[i] += 1
        nLen = 0
        for i in need.values():
            if i > 0:
                nLen += 1

        while right < sLen:
            c1 = s[right]
            right += 1
            if need[c1] > 0:
                window[c1] += 1
                if need[c1] == window[c1]:
                    matched += 1

            while matched == nLen:
                # 更新最小字串结果
                if right - left < res:
                    res = right - left
                    start = left
                c2 = s[left]
                left += 1

                if need[c2] > 0:
                    if window[c2] == need[c2]:
                        matched -= 1
                    window[c2] -= 1

        return "" if res == sLen + 1 else s[start: start+res]


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.lengthOfLongestSubstring(("abcabcbb")))
    # print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("aa", "aa"))


