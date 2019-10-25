from collections import OrderedDict

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         unique_char_dict = OrderedDict()
#         for idx, char in enumerate(s):
#             if char in unique_char_dict:
#                 unique_char_dict[char] = -1
#             else:
#                 unique_char_dict[char] = idx
#         for k, v in unique_char_dict.items():
#             if v != -1:
#                 return v
#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = dict()
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i
        return -1


s = 'leetcode'
print(Solution().firstUniqChar(s))

