class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(s, k, memo):
            if k == 0:
                return 1
            start = len(s) - k
            if s[start] == '0':
                return 0
            if memo[k]:
                return memo[k]
            result = helper(s, k - 1, memo)
            if k >= 2 and int(s[start: start + 2]) <= 26:
                result += helper(s, k - 2, memo)
            memo[k] = result
            return result
        memo = [None for _ in range(len(s) + 1)]
        return helper(s, len(s), memo)


print(Solution().numDecodings("226"))