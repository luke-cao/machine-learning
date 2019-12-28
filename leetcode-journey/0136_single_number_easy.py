from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         last_item = None
#         if len(nums) % 2:
#             last_item = nums.pop()
#         for i in range(0, len(nums), 2):
#             if nums[i] != nums[i + 1]:
#                 return nums[i]
#         return last_item


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


print(Solution().singleNumber([4, 1, 2, 1, 2]))
