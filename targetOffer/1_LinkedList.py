# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def __init__(self):
        self.result = []
    # 1. 返回从尾部到头部的列表值序列，例如[1,2,3]
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

    def Clone(self, pHead):
        """
        2. 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
        （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
        idea: 1. 把复制的结点链接在原始链表的每一对应结点后面(掌握，链表遍历和节点插入)
        2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
        3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，
        注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，next指针要重新赋值None(判定程序会认定你没有完成复制）
        :param pHead:
        :return:
        """
        if not pHead:
            return None
        dummy = pHead
        while dummy:
            nextHead = dummy.next
            copyHead = RandomListNode(dummy.label)
            copyHead.next = dummy.next
            dummy.next = copyHead
            dummy = nextHead

        dummy = pHead
        while dummy:
            copyHead = dummy.next
            if dummy.random:
                copy_dummy.random = dummy.random.next
            dummy = copy_dummy.next
            copy_dummy = dummy.next

    def FindKthToTail(self, head, k):
        """
        3.输入一个链表，输出该链表中倒数第k个结点
        idea: 双指针
        1)边界判断，head是否为空，k是否小于1，k是否大于链表长度
        :param head:
        :param k:
        :return:
        """
        if not head or k < 1:
            return None
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        if count < k:
            return None
        p1 = head
        p2 = head

        while k:
            p1 = p1.next
            k -= 1
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

    def ReverseList(self, pHead):
        """
        4.输入一个链表，反转链表后，输出新链表的表头。
        idea: 用一个头节点，然后头插法来实现链表反转
        :return:
        """
        if not pHead:
            return None
        head = ListNode(0)
        p = pHead
        while p:
            next = p.next
            p.next = head.next
            head.next = p
            p = next
        return head.next

    def Merge(self, pHead1, pHead2):
        """
        5. 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
        idea: 两个指针p1,p2分别指向两个两表，逐个比较大小，小的放入目标列表
        :param pHead1:
        :param pHead2:
        :return:
        """
        if not pHead1 and not pHead2:
            return None
        res = ListNode(0)
        head = res
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 =pHead2.next
            head = head.next
        if pHead1:
            head.next = pHead1
        if pHead2:
            head.next = pHead2
        return res.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node4 = ListNode(7)
    node5 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.printListFromTailToHead(node1))
    print(solution.printListFromTailToHead1(node1))

    p1 = ListNode(2)
    p2 = ListNode(6)
    p3 = ListNode(7)
    p1.next = p2
    p2.next = p3
    res5 = solution.Merge(node1, p1)

    p = res5
    while p:
        print("Merge: ", p.val)
        p = p.next
