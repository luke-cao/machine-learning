class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = -1
        for a in s:
            if t.find(a, idx + 1) >= 0:
                idx = t.find(a, idx + 1)
            else:
                return False
        return True


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) == 0:
#             return True
#         s_ptr = 0
#         for i in t:
#             if i == s[s_ptr]:
#                 s_ptr += 1
#             if s_ptr >= len(s):
#                 return True
#         return False
