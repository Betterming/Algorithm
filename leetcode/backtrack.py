import copy
class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, track):
            if len(nums) == len(track):
                res.append(track[:])  # 一定要用track[:] 而不能用track，因为track是引用，当后面改变track时，res对应当track也会改变，所以取当前track的副本放入res中，这时track再改变不会影响到这个副本
                return
            for item in nums:
                if item in track:
                    continue
                track.append(item)

                backtrack(nums, track)
                track.remove(item)
        track = []
        backtrack(nums, track)
        return res

    def NQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]

        def valid(row, col, board):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            j, k, l = row - 1, col-1, col + 1
            while j >= 0 and k >= 0:
                if board[j][k] == 'Q':
                    return False
                j -= 1
                k -= 1
            while j >= 0 and l < len(board[0]):
                if board[j][l] == 'Q':
                    return False
                j -= 1
                l += 1
            return True

        def backtrack(board, row):
            if row == len(board):
                res.append(copy.deepcopy(board))
                return

            # 选择列表：该row行上的所有元素
            # 路径：board上已经放上皇后的列号
            # 终止条件：row到达了最后一行
            cols = len(board[0])
            for i in range(cols):
                if not valid(row, i, board):
                    continue
                board[row][i] = 'Q'
                backtrack(board, row+1)
                board[row][i] = '.'

        backtrack(board, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))

    print(solution.NQueens(4))
