# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum_ = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            self.sum_ += node.val
            node.val = self.sum_
            inorder(node.left)
        inorder(root)
        return root