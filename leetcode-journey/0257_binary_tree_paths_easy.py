# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def helper(root: TreeNode, curr: str) -> None:
            if not root:
                return

            if not root.left and not root.right:
                res.append(curr + str(root.val))
                return
            else:
                helper(root.left, curr + str(root.val) + '->')
                helper(root.right, curr + str(root.val) + '->')

        res = []
        helper(root, '')
        return res