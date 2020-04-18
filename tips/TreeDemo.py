class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def postOrder(self, pre, tin):
        root = self.getTree(pre, tin)
        return self.getPostOrder(root)

    def getTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        root.left = self.getTree(pre[1: index + 1], tin[:index])
        root.right = self.getTree(pre[index + 1:], tin[index + 1:])
        return root

    def getPostOrder(self, root):
        if not root:
            return None

        self.getPostOrder(root.left)
        self.getPostOrder(root.right)
        self.result.append(root.val)
        return self.result

    def getPostOrder2(self, pre, tin):
        if not pre or not tin:
            return None
        if len(pre) == 1:
            return pre[0]
        index = tin.index(pre[0])
        return self.getPostOrder2(pre[1:index+1], tin[:index]) + self.getPostOrder2(pre[index+1:], tin[index+1:]) + pre[0]

import sys

try:
    origin = sys.stdin.readline().strip()
    solution = Solution()
    pre, tin = origin.split(' ')
    # result = solution.postOrder(pre, tin)
    result = solution.getPostOrder2(pre, tin)
    print(''.join(result))

except:
    pass
