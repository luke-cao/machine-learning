class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def are_identical(self, list_b):
        a = self.head
        b = list_b.head
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def push(self, value):
        new_node = Node(value)
        self.head, new_node.next = new_node, self.head


list1 = LinkedList()
list2 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list2.push(1)
list2.push(2)
list2.push(3)
if list1.are_identical(list2):
    print('Identical')
else:
    print('Not Identical')