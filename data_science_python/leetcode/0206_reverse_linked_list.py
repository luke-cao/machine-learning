# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        dummy_node = ListNode(0)
        pointer = dummy_node
        for i in reversed(stack):
            pointer.next = ListNode(i)
            pointer = pointer.next
        return dummy_node.nextgit
