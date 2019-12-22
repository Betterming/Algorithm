# -*- coding:utf-8 -*-
class Solution:
    """栈、队列
    1. 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
    例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    （注意：这两个序列的长度是相等的）
    """
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        if len(pushV) != len(popV):
            return False

        stack = []
        for item in pushV:
            stack.append(item)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    # 1. array: 二维数组， target给定数值
    array = [[1, 3, 4], [2, 5, 7], [10, 12, 14]]
    target1 = 12
    target2 = 13
    res1 = solution.Find(target1, array)
    # res12 = solution.Find(target12, array)
    print("1. result: %s" % res1)
