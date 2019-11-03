from typing import List

# time limit exceeded
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 last_num = 0 - nums[i] - nums[j]
#                 if last_num in nums[j + 1:]:
#                     triplet = sorted([nums[i], nums[j], last_num])
#                     if triplet not in triplets:
#                         triplets.append(triplet)
#         return triplets


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] < 0:
                continue
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                    while right - 1 > left and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
nums2 = [0,0,0,0]
print(Solution().threeSum(nums2))