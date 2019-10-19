class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = 0 # kid
        count = 0 # number of content kids
        for cookie in s:
            if i > len(g) - 1:
                return count
            if cookie >= g[i]:
                count += 1
                i += 1
        return count
