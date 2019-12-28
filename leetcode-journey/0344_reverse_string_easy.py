from typing import List

# Time limit exceed
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         count = 0
#         while count < len(s) - 1:
#             for i in range(len(s) - 1 - count):
#                 s[i], s[i + 1] = s[i + 1], s[i]
#             count += 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


input = ["H", "a", "n", "n", "a", "h"]
Solution().reverseString(input)
print(input)
assert input == ["h", "a", "n", "n", "a", "H"], 'Wrong'
