# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        Travel through the binary tree, and find all paths that comply to the question.
        using backtracking
        :param root:
        :param sum:
        :return:
        """
        def find_path(root: TreeNode, left_amt: int):
            nonlocal count
            left_amt -= root.val
            if left_amt == 0:
                count += 1
            if root.left:
                find_path(root.left, left_amt)
            if root.right:
                find_path(root.right, left_amt)

        def travel_through_binary_tree(root):
            find_path(root, sum)
            if root.left:
                travel_through_binary_tree(root.left)
            if root.right:
                travel_through_binary_tree(root.right)

        count = 0
        if root:
            travel_through_binary_tree(root)
        return count
