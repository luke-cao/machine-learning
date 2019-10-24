from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums) + 0) / 2 * (len(nums) + 1) - sum(nums))


print(Solution().missingNumber([3, 0, 1]))