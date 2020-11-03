import sys


class Solution1:
    """
    矩阵旋转
    逆时针旋转矩阵90度，但是不能利用额外的空间，只能使用本矩阵操作。
    逆时针旋转矩阵90度等于 对角线对称交换再i行与n-1-i行交换
    对角线对称元素关系：
    nums[i][j], nums[j][i]

    i行与n-1-i行元素关系：
    nums[i][j], nums[n-1-i][j]

    反对角线对称元素关系：
    nums[i][j], nums[n-1-j][n-1-i]

    """
    def transpose(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        for i in range(n//2):
            for j in range(n):
                nums[i][j], nums[n-1-i][j] = nums[n-1-i][j], nums[i][j]
        return nums

    def clockwise(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n-i):
                nums[i][j], nums[n-1-j][n-1-i] = nums[n-1-j][n-1-i], nums[i][j]
        for i in range(n//2):
            for j in range(n):
                nums[i][j], nums[n-1-i][j] = nums[n-1-i][j], nums[i][j]
        return nums

    def print2mat(self, a):
        n = len(a)
        for i in range(n):
            for j in range(n):
                if j < n-1:
                    print(a[i][j], end=' ')
                elif i < n-1:
                    print(a[i][j])
                else:
                    print(a[i][j], end='')

    def multiply2mat(self, a, b):
        am, an = len(a), len(a[0])
        bm, bn = len(b), len(b[0])
        if an != bm:
            return
        res = []
        for i in range(am):
            item = []
            rowA = a[i]
            for j in range(bn):
                colB = [x[j] for x in b]
                res_item = 0
                for r, c in zip(rowA, colB):
                    res_item += r*c
                    print(res_item)
                item.append(res_item)
            res.append(item)
        return res





if __name__ == '__main__':
    nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    import copy
    solution1 = Solution1()
    numsCopy = copy.deepcopy(nums)
    print("origin")
    solution1.print2mat(nums)
    print()
    print('-------')

    print('transpose')
    a = solution1.transpose(nums)
    solution1.print2mat(a)
    print()
    print('-------')

    print("clockwise")
    b = solution1.clockwise(numsCopy)
    solution1.print2mat(b)

    res1 = solution1.multiply2mat([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    print(res1)