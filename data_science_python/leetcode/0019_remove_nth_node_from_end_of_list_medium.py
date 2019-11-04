from leetcode import tools

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next


input1 = "[1,2,3,4,5]"
input2 = '[1]'
head = tools.stringToListNode(input2)
head = Solution().removeNthFromEnd(head, 1)
while head:
    print(head.val)
    head = head.next
