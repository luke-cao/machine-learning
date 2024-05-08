class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = max_current = nums[0]
        for i in range(1, len(nums)):
            max_current = max(max_current + nums[i], nums[i])
            max_global = max(max_global, max_current)
        return max_global
