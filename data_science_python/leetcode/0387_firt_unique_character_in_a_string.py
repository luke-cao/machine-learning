from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_char_dict = OrderedDict()
        for idx, char in enumerate(s):
            if char in unique_char_dict:
                unique_char_dict[char] = -1
            else:
                unique_char_dict[char] = idx
        for k, v in unique_char_dict.items():
            if v != -1:
                return v
        return -1


s = ''
print(Solution().firstUniqChar(s))

