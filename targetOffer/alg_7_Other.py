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

    def GetUglyNumber_Solution(self, index):
        """hard
        2. 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
         习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

        通俗易懂的解释：
        首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z，换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到，那么我们从1开始乘以2,3,5，就得到2,3,5三个丑数，在从这三个丑数出发乘以2,3,5就得到4，6,10,6，9,15,10,15,25九个丑数，我们发现这种方***得到重复的丑数，而且我们题目要求第N个丑数，这样的方法得到的丑数也是无序的。那么我们可以维护三个队列：
        （1）丑数数组： 1
        乘以2的队列：2
        乘以3的队列：3
        乘以5的队列：5
        选择三个队列头最小的数2加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （2）丑数数组：1,2
        乘以2的队列：4
        乘以3的队列：3，6
        乘以5的队列：5，10
        选择三个队列头最小的数3加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （3）丑数数组：1,2,3
        乘以2的队列：4,6
        乘以3的队列：6,9
        乘以5的队列：5,10,15
        选择三个队列头里最小的数4加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （4）丑数数组：1,2,3,4
        乘以2的队列：6，8
        乘以3的队列：6,9,12
        乘以5的队列：5,10,15,20
        选择三个队列头里最小的数5加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （5）丑数数组：1,2,3,4,5
        乘以2的队列：6,8,10，
        乘以3的队列：6,9,12,15
        乘以5的队列：10,15,20,25
        选择三个队列头里最小的数6加入丑数数组，但我们发现，有两个队列头都为6，所以我们弹出两个队列头，同时将12,18,30放入三个队列；
        ……………………
        疑问：
        1.为什么分三个队列？
        丑数数组里的数一定是有序的，因为我们是从丑数数组里的数乘以2,3,5选出的最小数，一定比以前未乘以2,3,5大，同时对于三个队列内部，按先后顺序乘以2,3,5分别放入，所以同一个队列内部也是有序的；
        2.为什么比较三个队列头部最小的数放入丑数数组？
        因为三个队列是有序的，所以取出三个头中最小的，等同于找到了三个队列所有数中最小的。
        实现思路：
        我们没有必要维护三个队列，只需要记录三个指针显示到达哪一步；“|”表示指针,arr表示丑数数组；
        （1）1
        |2
        |3
        |5
        目前指针指向0,0,0，队列头arr[0] * 2 = 2,  arr[0] * 3 = 3,  arr[0] * 5 = 5
        （2）1 2
        2 |4
        |3 6
        |5 10
        目前指针指向1,0,0，队列头arr[1] * 2 = 4,  arr[0] * 3 = 3, arr[0] * 5 = 5
        （3）1 2 3
        2| 4 6
        3 |6 9
        |5 10 15
        目前指针指向1,1,0，队列头arr[1] * 2 = 4,  arr[1] * 3 = 6, arr[0] * 5 = 5
        :param index:
        :return:
        """
        if index < 0:
            return None
        if index < 7:
            return index
        arr = []
        p1 = 0
        p2 = 0
        p3 = 0
        i = 0
        newData = 1
        arr.append(newData)
        while len(arr) < index:
            newData = min(arr[p1] * 2, arr[p2] * 3, arr[p3] * 5)
            arr.append(newData)
            if newData == arr[p1] * 2:
                p1 += 1
            if newData == arr[p2] * 3:
                p2 += 1
            if newData == arr[p3] * 5:
                p3 += 1

        return newData

    def reOrderArray(self, array):
        """
        3. 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
        所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
        idea: 遍历数组，奇数偶数各放一个数组，然后合并
        :param array:
        :return:
        """
        if not array or len(array) == 0:
            return []
        odd, even = [], []
        for i in array:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even

    def reOrderArray2(self, array):
        array.sort(key=lambda item:item % 2, reverse=True)
        return array

    def printMatrix(self, matrix):
        """
        4. 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
        idea: 可以打印第一行，然后删除第一行，再将剩下的数组逆转90°，重复此操作。
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        newMat = []
        for i in range(col):
            newMat2 = []
            for j in range(row):
                newMat2.append(matrix[j][i])
            newMat.append(newMat2)
        newMat.reverse()
        return newMat

    def printMatrix2(self, matrix):
        """
        idea: 观察二维数组发现，可以逐层打印，先最外一层打印完了
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        res = []
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = col - 1
        top = 0
        bottom = row - 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):  # left to right
                res.append(matrix[top][i])
            for i in range(top+1, bottom+1): # top to bottom
                res.append(matrix[i][right])
            if top < bottom:
                for i in range(right-1, left-1, -1): # right to left
                    res.append(matrix[bottom][i])
            if left < right:
                for i in range(bottom-1, top, -1): # bottom to top
                    res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return res

    def MoreThanHalfNum_Solution(self, numbers):
        """array tips
        5. 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
        :param numbers:
        :return:
        """
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2.0:
            return count[0][0]
        return 0


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.GetUglyNumber_Solution(0)
    print("GetUglyNumber_Solution: %s" % res1)

    res2 = solution.Find(4, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
    print("Find: %s" % res2)

    res3 = solution.reOrderArray([2, 10, 1, 3, 4, 5, 23, 1])
    print("reOrderArray: ", res3)

    res32 = solution.reOrderArray2([2, 10, 1, 3, 4, 5, 23, 1])
    print("reOrderArray2: ", res32)
    res4  = solution.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("printMatrix: ", res4)
    res42  = solution.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("printMatrix: ", res42)

    res5 = solution.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
    print("MoreThanHalfNum_Solution: ", res5)

