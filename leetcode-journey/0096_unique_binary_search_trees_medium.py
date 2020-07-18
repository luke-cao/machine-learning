class Solution:
    cache = {}

    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        if self.cache.get(n):
            return self.cache[n]
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - 1 - i)
        self.cache[n] = res
        return res


print(Solution().numTrees(18))
