# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         """
#         Travel through the binary tree, and find all paths that comply to the question.
#         using backtracking
#         :param root:
#         :param sum:
#         :return:
#         """
#         def find_path(root: TreeNode, left_amt: int):
#             nonlocal count
#             left_amt -= root.val
#             if left_amt == 0:
#                 count += 1
#             if root.left:
#                 find_path(root.left, left_amt)
#             if root.right:
#                 find_path(root.right, left_amt)
#
#         def travel_through_binary_tree(root):
#             find_path(root, sum)
#             if root.left:
#                 travel_through_binary_tree(root.left)
#             if root.right:
#                 travel_through_binary_tree(root.right)
#
#         count = 0
#         if root:
#             travel_through_binary_tree(root)
#         return count


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def recursion(rt: TreeNode, target, stack: list):
            if not rt:
                return 0
            count = 0
            for idx, num in enumerate(stack):
                stack[idx] += rt.val
                if num + rt.val == sum:
                    count += 1
            if rt.val == sum:
                count += 1
            stack.append(rt.val)
            stack_left = stack.copy()
            stack_right = stack.copy()
            return count + recursion(rt.left, target, stack_left) + recursion(rt.right, target, stack_right)

        return recursion(root, sum, [])


def stringToTreeNode(input):
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
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);

            ret = Solution().pathSum(root, sum)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

