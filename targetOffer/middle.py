class Solution1:
    # 1. 两个序列， 第一个序列是入栈顺序，第二个是出战顺序，判断出栈是否正确
    # idea：
    # 1) 边界校验
    # 2) 序列pushV逐个入栈
    # 3) 每次入栈都要对整个栈从栈顶循环与popV头元素判断，相等弹出栈顶元素和popV头元素
    # 4) 最后对栈大小判断，为0true，否则false
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        if len(pushV) != len(popV):
            return False

        stack =[]
        for item_push in pushV:
            stack.append(item_push)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if len(stack) == 0:
            return True
        else:
            return False


# 2. 两个栈实现一个队列
class Solution2:
    # idea:
    # 1. 两个栈stack1，stack2，push正常入栈
    # 2. pop时，当stack2有值时直接从stack2弹出元素，当stack2无值时，若stack1也无值，直接返回None
    # 若stack1有值时，将stack1所有元素都移到stack2中，再从stack2中弹出
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return len(self.stack2) + len(self.stack1)


if __name__ == '__main__':
    solution1 = Solution1()
    pushV = [1, 2, 3, 4, 5]
    popV1 = [4, 5, 3, 2, 1]
    popV2 = [4, 3, 5, 1, 2]
    res11 = solution1.IsPopOrder(pushV, popV1)
    res12 = solution1.IsPopOrder(pushV, popV2)
    print("1：res1: {0}, res2: {1}".format(res11, res12))

    solution2 = Solution2()
    q = solution2
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    q.pop()
    q.pop()

    while q.size():
        print(q.pop())



