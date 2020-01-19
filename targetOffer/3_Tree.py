class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def layerOrder(root):
    queue = []
    queue.append(root)

    while queue:
        out = queue.pop(0)
        print(out.val)
        if out.left:
            queue.append(out.left)
        if out.right:
            queue.append(out.right)

class Solution:
    # 1. 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    # 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回
    # 思路：根据前序遍历找到根结点，用根结点在中序遍历中切开左右子树，递归重建二叉树
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin) -> TreeNode:
        if not pre:
            return None

        root = TreeNode(pre[0])
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root

    def PrintFromTopToBottom(self, root):
        """
        2.从上往下打印出二叉树的每个节点，同层节点从左至右打印。
        idea: 典型的层序遍历，用队列解决
        :param root:
        :return:
        """
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while len(queue):
            res.append(queue[0].val)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        return res

    def VerifySquenceOfBST(self, sequence):
        """
        3. 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
        如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
        idea: 分治递归思想，首先要知道BST的基本性质，左<根<右，然后知道最后一个数为根结点，通过根节点值切割左右子树。
        :param sequence:
        :return:
        """
        if not sequence:
            return False
        length = len(sequence)
        root = sequence[length - 1]
        # 找出比root大的第一个节点，如果没有的话i就等于最后一个节点
        for i in range(length):
            if sequence[i] > root:
                break
        for j in range(i, length-1):
            if sequence[j] < root:
                return False
        left = right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i < length - 1 and left:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right


class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.array = []
        self.result_all = []
        self.preResult = []
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.array.pop()
        return self.result_all


    def preOrder(self, root, layer):
        """
        二叉树的先序遍历
        :param root:
        :return:
        """
        if not root:
            return
        self.preResult.append(root.val)
        self.preOrder(root.left, layer + 1)
        self.preOrder(root.right, layer + 1)
        return self.preResult


if __name__ == '__main__':
    solution = Solution()
    root = solution.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])
    layerOrder(root)
    res31 = solution.VerifySquenceOfBST([7,4,6,5])
    res32 = solution.VerifySquenceOfBST([1,4,6,5])

    print("VerifySquenceOfBST: ", res31)
    print("VerifySquenceOfBST: ", res32)

    solution2 = Solution2()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    res4 = solution2.FindPath(root, 19)
    print("FindPath: ", res4)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    preOrderResult = solution2.preOrder(a, 0)
    print("preOrder ", preOrderResult)