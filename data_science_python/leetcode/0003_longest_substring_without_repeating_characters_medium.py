class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window [i, j), left-closed, right-open
        time complexity:
        space complexity:
        :param s:
        :return:
        """
        max_length = 0
        start = 0
        for i in range(len(s)):
            if s[start: i].find(s[i]) >= 0:
                start += s[start: i].find(s[i]) + 1
            else:
                max_length = max(max_length, i - start + 1)
        return max_length


print(Solution().lengthOfLongeubstring("bbtablud"))
