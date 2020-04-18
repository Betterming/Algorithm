# -*- coding:utf-8 -*-
class Solution:
    """
    8. 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    这是一个斐波那契数列
    """
    def jumpFloor(self, number):
        # write code here
        if number < 0:
            return 0
        if number <= 3:
            return number
        return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)

    def jumpFloor2(self, number):
        # write code here
        if number < 0:
            return 0
        if number < 4:
            return number
        j1 = 1
        j2 = 2
        for _ in range(number-2):
            j2, j1 = j2 + j1, j2
        return j2

    def hasPath(self, matrix, rows, cols, path):
        # 65.请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
        # 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，
        # 向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
        # 例如 \begin{bmatrix} a & b & c &e \\ s & f & c & s \\ a & d & e& e\\ \end{bmatrix}\quad
        # 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
        # 因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols * i:cols * i + cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False

    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i - 1, j, p[1:]):
                return True
            if i < len(matrix) - 1 and self.exist_helper(matrix, i + 1, j, p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j - 1, p[1:]):
                return True
            if j < len(matrix[0]) - 1 and self.exist_helper(matrix, i, j + 1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False

    def movingCount(self, threshold, rows, cols):
        # 66. 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
        # 但是不能进入行坐标和列坐标的数位之和大于k的格子。
        # 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
        # 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
        array = []
        for i in range(rows):
            res = []
            for j in range(cols):
                res.append(getN(i, j))
            array.append(res)
        from pprint import pprint
        pprint(array)
        visited = [[0] * len(array[0]) for _ in range(len(array))]
        return self.DFS(array, 0, 0, threshold, visited)

    def getN(self, i, j):
        res = 0
        while i:
            res += (i % 10)
            i //= 10
        while j:
            res += (j % 10)
            j //= 10
        return res

    def DFS(self, array, i, j, threshold, visited):
        if i < 0 or j < 0 or i > len(array)-1 or j > len(array[0])-1 \
                or array[i][j] > threshold or visited[i][j]:
            return 0
        res = 1
        visited[i][j] = 1
        res += self.DFS(array, i + 1, j, threshold, visited)
        res += self.DFS(array, i - 1, j, threshold, visited)
        res += self.DFS(array, i, j + 1, threshold, visited)
        res += self.DFS(array, i, j - 1, threshold, visited)
        return res


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.jumpFloor(5)
    print("jumpFloor: ", res1)
