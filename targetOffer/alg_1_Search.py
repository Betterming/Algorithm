# -*- coding:utf-8 -*-
class Solution:
    """medium
    1. 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    """
    # idea1： 逐个比较,O(n), O(1)
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        minRes = rotateArray[0]
        for item in rotateArray:
            if item < minRes:
                minRes = item
        return minRes

    # idea2: 二分查找
    def minNumberInRotateArray2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        rot_len = len(rotateArray)
        left = 0
        right = rot_len - 1
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if (right - left) == 1:
                mid = right
                break
            mid = left + (right - left) // 2
            if rotateArray[left] == rotateArray[right] and rotateArray[left] == rotateArray[mid]:
                return self.MinOrder(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]

    def MinOrder(self, rotateArray, left, right):
        result = rotateArray[left]
        for item in rotateArray[left+1, right]:
            if item < result:
                result = item
        return result


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.minNumberInRotateArray([3, 4, 5, 1, 2])
    res2 = solution.minNumberInRotateArray2([3, 4, 5, 1, 2])
    print("minNumberInRotateArray: %s" % res1)
    print("minNumberInRotateArray2: %s" % res2)
