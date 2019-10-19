class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for e, l in zip(reversed(range(len(s))), s):
            num += (ord(l) - ord('A') + 1) * 26 ** e
        return num


print(Solution().titleToNumber('AB'))