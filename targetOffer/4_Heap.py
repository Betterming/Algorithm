class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """heap
        29. 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
        :param tinput:
        :param k:
        :return:
        """
        if k > len(tinput):
            return []
        import heapq
        return heapq.nsmallest(k, tinput)

if __name__ == '__main__':
    solution = Solution()
    res6 = solution.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 3)
    print("GetLeastNumbers_Solution: ", res6)