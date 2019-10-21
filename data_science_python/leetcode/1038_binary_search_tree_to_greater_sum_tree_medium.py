from leetcode import tools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    total = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def right_mid_left_order(node: TreeNode):
            if node is None:
                return 0
            right_mid_left_order(node.right)
            self.total += node.val
            node.val = self.total
            right_mid_left_order(node.left)

        right_mid_left_order(root)
        return root


if __name__ == '__main__':
    test_case = '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
    root = tools.stringToTreeNode(test_case)
    root = Solution().bstToGst(root)
    print(tools.treeNodeToString(root))