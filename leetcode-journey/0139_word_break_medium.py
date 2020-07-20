from typing import List

class Solution:
    """out of time limit"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        res = False
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                res = True and self.wordBreak(s[i + 1:], wordDict)
            if res:
                return res
        return res

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        can_break = [1] + [0] * n
        for loc in range(n):
            if not can_break[loc]:
                continue
            for word in wordDict:
                if s[loc: loc + len(word)] == word:
                    can_break[loc + len(word)] = 1
        return can_break[-1]


print(Solution().wordBreak('leetcode', ["leet", "code"]))