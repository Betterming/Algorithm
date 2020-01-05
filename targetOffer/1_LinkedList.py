# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.result = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 解法1：用辅助栈存储
    def printListFromTailToHead1(self, listNode):
        # write code here
        stack = []
        result_array = []
        node_p = listNode
        while node_p:
            stack.append(node_p.val)
            node_p = node_p.next
        while stack:
            result_array.append(stack.pop(-1))
        return result_array

    # 解法2：用递推
    # 思路：
    # 1. 想要将n个值列表反转放进result_array数组中，可以先将后面n-1个节点值放入result_array数组，然后第一个节点值在放入
    # 2. 若想将后n-1个值列表反转放进result_array数组中，可以先将后面n-2个节点值放入result_array数组，然后第二个节点值在放入，依次类推。。。
    # 3. 边界：最后一个值想要放入result_array数组中，则先将最后一个值的next节点的值即None放入result_array数组中，
    # 而当printListFromTailToHead的入参为None时结束递归，进行下一步，将最后一个值放入result_array中，依次反向带入值，完成原列表反向所有值放入到result_array中
    def printListFromTailToHead(self, listNode):
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.result.append(listNode.val)
        return self.result


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.printListFromTailToHead(node1))
    print(solution.printListFromTailToHead1(node1))