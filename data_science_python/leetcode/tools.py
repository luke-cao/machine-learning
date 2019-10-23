import os
import re

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


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def count_file_num_of_folder(folder):
    counts = {'Easy': 0, 'Medium': 0, 'Hard': 0, 'Other': 0}
    for i in os.listdir(folder):
        if re.search(r'\d+_.*_[a-z]+\.py', i):
            if i.endswith('easy.py'):
                counts['Easy'] += 1
            elif i.endswith('medium.py'):
                counts['Medium'] += 1
            elif i.endswith('hard.py'):
                counts['Hard'] += 1
            else:
                counts['Other'] += 1
    return f'Leedcode Problem Have Been Solved Stats: \n{counts}'


if __name__ == '__main__':
    folder = '.'
    print(count_file_num_of_folder(folder))
