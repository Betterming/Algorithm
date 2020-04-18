class Solution:
    def __init__(self):
        self.cnt = 0

    def mergeSort(self, array):
        """
        归并排序：将n个元素分成两部分，左右两部分再递归使用归并排序，直到所有部分的元素个数都为1为止
        从最底层开始从上合并成两个排好序的数列
        采用的方法是分治递归法
        :param array:
        :return:
        """
        if not len(array):
            return None
        res = [0] * len(array)
        self.mergeSort2(array, 0, len(array)-1, res)
        return res

    def mergeSort2(self, array, first, last, res):
        if first < last:
            mid = first + (last - first) // 2
            self.mergeSort2(array, first, mid, res)
            self.mergeSort2(array, mid+1, last, res)
            self.mergeArray(array, first, mid, last, res)

    def mergeArray(self, array, first, mid, last, res):
        i = first
        j = mid + 1
        m = mid
        n = last
        k = 0
        while i <= m and j <= n:
            if array[i] <= array[j]:
                res[k] = array[i]
                k += 1
                i += 1
            else:
                res[k] = array[j]
                k += 1
                j += 1

        while i <= m:
            res[k] = array[i]
            k += 1
            i += 1

        while j <= n:
            res[k] = array[j]
            k += 1
            j += 1

        for i in range(k):
            array[first + i] = res[i]

    def InversePairs(self, data):
        """
        35.在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
        输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
        输入描述:题目保证输入的数组中没有的相同的数字
        数据范围：
            对于%50的数据,size<=10^4
            对于%75的数据,size<=10^5
            对于%100的数据,size<=2*10^5

        示例1
        输入
        1,2,3,4,5,6,7,0
        输出
        7

        idea:暴力法时间复杂度是o(n^2)，超时。逆序是说a[i]>a[j]，i<j。
        那么在排序的过程中，会把a[i]和a[j]交换过来，这个交换的过程，每交换一次，就是一个逆序对的“正序”过程。
        排序每个数，归并排序。
        :param data:
        :return:
        """
        self.mergeSortPairs(data, 0, len(data) - 1)
        return self.cnt

    def mergeSortPairs(self, array, start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        self.mergeSortPairs(array, start, mid)
        self.mergeSortPairs(array, mid + 1, end)
        self.mergeOne(array, start, mid, end)

    def mergeOne(self, array, start, mid, end):
        temp = [0] * (end - start + 1)
        k = 0
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if array[i] <= array[j]:
                temp[k] = array[i]
                k += 1
                i += 1
            else:
                temp[k] = array[j]
                k += 1
                j += 1
                self.cnt = (self.cnt + mid - i + 1) % 1000000007
        while i <= mid:
            temp[k] = array[i]
            k += 1
            i += 1
        while j <= end:
            temp[k] = array[j]
            k += 1
            j += 1
        # 将temp值返给原array，用于下一步的比较归并
        for i in range(k):
            array[start + i] = temp[i]

    def reOrderArray(self, array):
        """
        13. 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
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
        array.sort(key=lambda item: item % 2, reverse=True)
        return array


if __name__ == '__main__':
    solution = Solution()
    res3 = solution.reOrderArray([2, 10, 1, 3, 4, 5, 23, 1])
    print("reOrderArray: ", res3)

    res32 = solution.reOrderArray2([2, 10, 1, 3, 4, 5, 23, 1])
    print("reOrderArray2: ", res32)

    res1 = solution.mergeSort([2, 1, 3, 5, 7, 6, 4])
    cnt = solution.InversePairs([3, 2, 1])
    print("res", res1)
    print("mergeSortPairs", cnt)
