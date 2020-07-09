# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root: TreeNode) -> int:
            if not root:
                return 0

            left = get_height(root.left)
            right = get_height(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        # if is not balanced, will be -1
        return get_height(root) >= 0