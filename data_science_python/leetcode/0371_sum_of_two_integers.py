class Solution:
    def getSum(self, a: int, b: int) -> int:
        # get do subtraction while the code in java can do
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a


# print(Solution().getSum(2, 5))
print(Solution().getSum(-2, 3))

