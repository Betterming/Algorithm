class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


if __name__ == '__main__':
    solution = Solution()
    root = solution.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])
    layerOrder(root)
