from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global, max_local = nums[0], nums[0]
        for num in nums[1:]:
            max_local = max(max_local + num, num)
            max_global = max(max_global, max_local)
        return max_global


assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6,  Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
