import math


# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         n = math.factorial(n)
#         count = 0
#         for i in str(n)[::-1]:
#             if i != '0':
#                 break
#             count += 1
#         return count


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n != 0:
            result += n // 5
            n //= 5
        return result


print(Solution().trailingZeroes(1808548329))
