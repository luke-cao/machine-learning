# class Solution:
#     def reverse(self, x: int) -> int:
#         neg = False
#         if x < 0:
#             x = abs(x)
#             neg = True
#         x = (str(x)[::-1]).lstrip('0')
#         if not x:
#             x = 0
#         x = -int(x) if neg else int(x)
#         if x < -(2 ** 31) or x > 2 ** 31 - 1:
#             return 0
#         else:
#             return x

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        neg_flg = False
        if x < 0:
            neg_flg = True
            x = -x
        result = 0
        while x > 0:
            remainder = x % 10
            x //= 10
            result = result * 10 + remainder
        result = -result if neg_flg else result
        if -(2 ** 31) <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0


print(Solution().reverse(1534236469))
assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(1534236469) == 0
assert Solution().reverse(120) == 21
