# can't process negative number
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        while dividend >= divisor:
            dividend_1, divisor_1 = dividend, divisor
            count = 0
            while dividend_1 >= divisor_1:
                divisor_1 <<= 1
                count += 1
            divisor_1 >>= 1
            count -= 1
            ret += 2 ** count
            dividend -= divisor_1
        return ret


print(Solution().divide(7, -3))