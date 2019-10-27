from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums_set = set()
#         for num in nums:
#             if num in nums_set:
#                 return True
#             else:
#                 nums_set.add(num)
#         return False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


print(Solution().containsDuplicate([1, 2, 3, 4]))