class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        x = (str(x)[::-1]).lstrip('0')
        if not x:
            x = 0
        x = -int(x) if neg else int(x)
        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0
        else:
            return x


print(Solution().reverse(1534236469))
