import os


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def change_file_name(folder):
    for src in os.listdir(folder):
        if src.startswith('leetcode_'):
            dst = src.replace('leetcode_', '')
            os.rename(src, dst)


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


if __name__ == '__main__':
    tree_list = '[1,2,2,null,3,null,3]'
    root = stringToTreeNode(tree_list)
    print(root.val)
