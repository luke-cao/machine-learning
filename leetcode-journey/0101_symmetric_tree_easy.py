from leetcode import tools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_symmetric_recu(root.left, root.right)

    def is_symmetric_recu(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.is_symmetric_recu(left.left, right.right) and self.is_symmetric_recu(left.right, right.left)


if __name__ == '__main__':
    # e.g. [1,2,2,3,4,4,3] -> True
    binary_tree = input()
    root = tools.stringToTreeNode(binary_tree)
    print(Solution().isSymmetric(root))