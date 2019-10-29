class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        for i in range(len(s)):
            is_unique = True
            for j in range(start, i):
                if s[j] == s[i]:
                    start = j + 1
                    is_unique = False
                    break
            if is_unique:
                max_length = max(max_length, i - start + 1)
        return max_length


print(Solution().lengthOfLongestSubstring("pwwkew"))