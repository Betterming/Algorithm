class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def layerOrder(root):
    queue = [root]

    while queue:
        out = queue.pop(0)
        print(out.val)
        if out.left:
            queue.append(out.left)
        if out.right:
            queue.append(out.right)

class Solution:
    # 4. 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    # 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回
    # 思路：根据前序遍历找到根结点，用根结点在中序遍历中切开左右子树，递归重建二叉树
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None

        root = TreeNode(pre[0])
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root

    def PrintFromTopToBottom(self, root):
        """
        22.从上往下打印出二叉树的每个节点，同层节点从左至右打印。
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
        23. 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
        如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
        idea: 分治递归思想，首先要知道BST的基本性质，左<根<右，然后知道最后一个数为根结点，通过根节点值切割左右子树。
        1) 边界判断，从[0, length-1]中找到第一个比root大的值i
        2) 若[i,length-1)中有一个比root值小就False
        3) 默认left=right=True,i在(0, length-1)中对i左右两边递归判断，最后返回left and right
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

    def HasSubtree(self, pRoot1, pRoot2):
        """
        17.输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
        idea: 树的遍历，对树的每一个节点进行判别
        :param pRoot1:
        :param pRoot2:
        :return:
        """
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            if self.isSame(pRoot1, pRoot2):
                return True
            else:
                return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSame(self, p1, p2):
        if not p2:
            return True
        elif not p1:
            return False
        elif p1.val == p2.val:
            return self.isSame(p1.left, p2.left) and self.isSame(p1.right, p2.right)
        else:
            return False

    def Mirror(self, root):
        """
        18.操作给定的二叉树，将其变换为源二叉树的镜像。
        idea: 递归，将Mirror(root.left)看成已经操作完成后返回的根节点
        :param root:
        :return:
        """
        if not root:
            return None
        temp = self.Mirror(root.left)
        root.left = self.Mirror(root.right)
        root.right = temp
        return root

    def Convert(self, pRootOfTree):
        """
        26.输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
        :param pRootOfTree:
        :return:
        """
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        while left and p.right:
            p = p.right
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        return left if left else pRootOfTree

    def TreeDepth(self, pRoot):
        """
        求树的深度
        idea: 递归
        """

        if not pRoot:
            return 0
        if not pRoot.left and not pRoot.right:
            return 1
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    def IsBalanced_Solution(self, pRoot):
        """
        39. 判断一棵树是不是平衡二叉树、
        idea: 从下往上，递归判断：如果子树是平衡二叉树则返回高度，如果不是直接终止并返回-1
        :param pRoot:
        :return:
        """
        if not pRoot:
            return False
        return self.getDepth(pRoot) != -1

    def getDepth(self, root):
        """
        38.从下往上遍历，如果子树是平衡二叉树，则返回子树的高度；
        如果发现子树不是平衡二叉树，则直接停止遍历，返回-1，这样至多只对每个结点访问一次。
        :param root:
        :return:
        """
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        return -1 if int(abs(left - right)) > 1 else 1 + max(left, right)

    def GetNext(self, pNode):
        """
        57. 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
        注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
        idea:分成两大类：
        1、有右子树的，那么下个结点就是右子树最左边的点；（eg：D，B，E，A，C，G）
        2、没有右子树的，也可以分成两类，
            a)是父节点左孩子（eg：N，I，L） ，那么父节点就是下一个节点 ；
            b)是父节点的右孩子（eg：H，J，K，M）找他的父节点的父节点的父节点...
        直到当前结点是其父节点的左孩子位置。如果没有eg：M，那么他就是尾节点。
        :param pNode:
        :return:
        """
        if not pNode:
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p

        pNext = pNode.next
        if not pNext:
            return None
        if pNext.left == pNode:
            return pNext
        while pNext.next and pNext.next.left != pNext:
            pNext = pNext.next
        return pNext.next

    def isSymmetrical(self, pRoot):
        """
        58. 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
        idea: 递归判断：
        1)边界判断：pRoot为None,return True
        2)对子树递归判断：分三种情况：left和right均为None,有一个为None,均不为None
            a.均为None: return True
            b.有一个为None: return False
            c.均不为None: 若pRoot的左子树的左子树与右子树的右子树对称， 且pRoot的左子树的右子树与右子树的左子树对称，则为True，反之为False
        :param pRoot:
        :return:
        """
        # write code here
        if not pRoot:
            return True
        return self.isSym(pRoot.left, pRoot.right)

    def isSym(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)

    def Print59(self, pRoot):
        """
        59.请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
        第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
        idea: 层序打印
        :param pRoot:
        :return:
        """
        if not pRoot:
            return []
        res = []
        queue = [pRoot]
        j = -1
        while queue:
            j += 1
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if j % 2:
                temp.reverse()
            res.append(temp)
        return res

    def KthNode(self, pRoot, k):
        """
        62.给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
        idea: 中序遍历将值放入res中，k若在res范围内返回res[k-1],不在返回None
        :param pRoot:
        :param k:
        :return:
        """
        res = []
        self.dfs(pRoot, res)
        return res[k - 1] if 0 < k <= len(res) else None

    def dfs(self, root, res):
        if not root:
            return None
        self.dfs(root.left, res)
        res.append(root)
        self.dfs(root.right, res)

    def KthNode2(self, pRoot, k):
        """
        idea2: 中序遍历，count统计到k时退出
        :param pRoot:
        :param k:
        :return:
        """
        if not pRoot:
            return None
        count = 0
        res = -1
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            count += 1
            if count == k:
                res = count
                return
            dfs(root.right)
        dfs(pRoot)
        return res

    def Print(self, pRoot):
        """
        60. 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
        idea: 树的层序遍历，或者是广度遍历
        :param pRoot:
        :return:
        """
        if not pRoot:
            return []
        res = []
        queue = []
        queue.append(pRoot)
        start, end = 0, 1
        while len(queue):
            array = []
            temp = queue[0]
            queue.pop(0)
            array.append(temp)
            start += 1

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            if start == end:
                end = len(queue)
                start = 0
                res.append(array)
        return res


class Solution2:
    # 24.返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.array = []
        self.result_all = []
        self.preResult = []
        self.index = -1

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

    def Serialize(self, root):
        # 61.请实现两个函数，分别用来序列化和反序列化二叉树
        if root:
            return str(root.val) + ' ' + \
                   self.Serialize(root.left) + \
                   self.Serialize(root.right)
        else:
            return '# '

    def Deserialize(self, s):
        # write code here
        l = s.split()
        self.index += 1
        if self.index >= len(s):
            return None

        if l[self.index] != '#':
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            return None
        return root


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