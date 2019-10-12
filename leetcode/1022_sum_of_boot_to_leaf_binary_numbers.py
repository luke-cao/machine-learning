class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, [root.val])]
        paths = []
        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right:
                path = list(map(str, path))
                paths.append(''.join(path))
            if curr.left:
                stack.append((curr.left, path + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, path + [curr.right.val]))
        return sum(int(i, base=2) for i in paths)
