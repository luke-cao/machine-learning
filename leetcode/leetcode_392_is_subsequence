class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = -1
        for a in s:
            if t.find(a, idx + 1) >= 0:
                idx = t.find(a, idx + 1)
            else:
                return False
        return True
