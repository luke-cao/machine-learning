class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count

# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return bin(n).count('1')

print(Solution().hammingWeight(int('00000000000000000000000000001011', 2)))
print(Solution().hammingWeight(int('00000000000000000000000010000000', 2)))
print(Solution().hammingWeight(int('11111111111111111111111111111101', 2)))

