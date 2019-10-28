# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        l3 = dummy_node
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        if l1 is None and l2 is None:
            pass
        elif l1 is None:
            l3.next = l2
        else:
            l3.next = l1
        return dummy_node.next
