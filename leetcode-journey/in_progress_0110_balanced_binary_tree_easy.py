# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def travel_tree(root: TreeNode, depth=0):
            nonlocal high, low
            if not root.left or not root.right:
                if depth > high:
                    high = depth
                if depth < low:
                    low = depth
            if root.left:
                travel_tree(root.left, depth + 1)

            if root.right:
                travel_tree(root.right, depth + 1)

        from math import inf
        high, low = -inf, inf
        if not root:
            return True
        travel_tree(root)
        if high == -inf:
            high = 0
        if low == inf:
            low = 0
        return True if high - low <= 1 else False


def stringToTreedNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    
    def readline():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')
    
    lines = readline()
    while True:
        try:
            line = next(lines)
            root = stringToTreedNode(line)
            ret = Solution().isBalanced(root)
            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
