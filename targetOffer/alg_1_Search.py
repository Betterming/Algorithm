# -*- coding:utf-8 -*-
class Solution:
    """medium
    1. 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    idea: 从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。
    于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。
    """

    def Find(self, target, array):
        if not array or not target:
            return False
        row = len(array) - 1
        col = len(array[0]) - 1
        i = row
        j = 0
        while i >= 0 and j <= col:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False

    """medium
    6. 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
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

    def GetNumberOfK(self, data, k):
        """
        37. 统计一个数字在排序数组中出现的次数。
        idea1: 遍历统计
        :param data:
        :param k:
        :return:
        """
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count


    def GetNumberOfK2(self, data, k):
        """
        idea2: 利用数组的count方法
        :param data:
        :param k:
        :return:
        """
        return data.count(k)

    def GetNumberOfK3(self, data, k):
        """
        idea3: 二分查找
        :param data:
        :param k:
        :return:
        """
        return self.binarySearch(data, k+0.5) - self.binarySearch(data, k-0.5)

    def binarySearch(self, data, k):
        if len(data) <= 0:
            return None
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return high



if __name__ == '__main__':
    solution = Solution()
    res1 = solution.minNumberInRotateArray([3, 4, 5, 1, 2])
    res2 = solution.minNumberInRotateArray2([3, 4, 5, 1, 2])
    print("minNumberInRotateArray: %s" % res1)
    print("minNumberInRotateArray2: %s" % res2)

    res21 = solution.GetNumberOfK([2, 3, 3, 3, 3, 4, 5], 3)
    print("GetNumberOfK: ", res21)
    res22 = solution.GetNumberOfK([2, 3, 3, 3, 3, 4, 5], 3)
    print("GetNumberOfK: ", res22)
    res23 = solution.GetNumberOfK3([2, 3, 3, 4, 5], 3)
    print("GetNumberOfK: ", res23)
