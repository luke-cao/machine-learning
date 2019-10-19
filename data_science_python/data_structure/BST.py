class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, val):
        if val == self.val:
            return False
        elif val < self.val:
            if self.left_child:
                return self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(val)
            else:
                self.right_child = Node(val)
                return True

    def find(self, val):
        if val == self.val:
            return True
        elif val < self.val:
            if self.left_child:
                return self.left_child.find(val)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(val)
            else:
                return False

    def inorder(self) -> list:
        """
        left -> root - > right
        :return:
        """
        ret = []
        if self.left_child:
            ret.extend(self.left_child.inorder())
        ret.append(self.val)
        if self.right_child:
            ret.extend(self.right_child.inorder())
        return ret

    def preorder(self) -> list:
        """
        root -> left -> right
        :return:
        """
        ret = [self.val]
        if self.left_child:
            ret.extend(self.left_child.preorder())
        if self.right_child:
            ret.extend(self.right_child.preorder())
        return ret

    def postorder(self) -> list:
        """
        left -> right -> root
        :return:
        """
        ret = []
        if self.left_child:
            ret.extend(self.left_child.postorder())
        if self.right_child:
            ret.extend(self.right_child.postorder())
        ret.append(self.val)
        return ret


class BSTTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def find(self, val):
        if self.root:
            return self.root.find(val)
        else:
            return False

    def preorder(self) -> list:
        print('pre-order: ', end='')
        if self.root:
            return self.root.preorder()
        else:
            return []

    def inorder(self) -> list:
        print('in-order: ', end='')
        if self.root:
            return self.root.inorder()
        else:
            return []

    def postorder(self) -> list:
        print('post-order: ', end='')
        if self.root:
            return self.root.postorder()
        else:
            return []


if __name__ == '__main__':
    tree = BSTTree()
    print(tree.insert(8))
    print(tree.insert(3))
    print(tree.insert(10))
    print(tree.insert(1))
    print(tree.insert(6))
    print(tree.insert(14))
    print(tree.insert(4))
    print(tree.insert(7))
    print(tree.insert(13))

    print(tree.preorder())
    print(tree.inorder())
    print(tree.postorder())



