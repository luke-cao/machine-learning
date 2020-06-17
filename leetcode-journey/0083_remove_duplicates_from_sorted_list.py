# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current:
            runner = current.next
            while runner and runner.val == current.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head

