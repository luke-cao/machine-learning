# class Solution:
#     def mySqrt(self, x: int) -> int:
#         factor = 0
#         while factor * factor <= x:
#             factor += 1
#         return factor - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return int(left - 1)

print(Solution().mySqrt(9))