from leetcode import tools

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         while head:
#             vals.append(head.val)
#             head = head.next
#         i, j = 0, len(vals) - 1
#         while i <= j:
#             if vals[i] != vals[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         if fast:
#             slow = slow.next
#         while slow:
#             if head.val != slow.val:
#                 return False
#             head = head.next
#             slow = slow.next
#         return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and slow and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return rev is None


input = [1, 2, 2, 1]
head = tools.stringToListNode(str(input))
print(Solution().isPalindrome(head))