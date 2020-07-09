from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        current = [root]
        result = []
        while current:
            next_level = []
            temp = []
            for i in current:
                temp.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            result.append(temp)
            current = next_level
        return result[::-1]