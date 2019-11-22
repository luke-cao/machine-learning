from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, middle, right = 0, 0, len(nums) - 1
        while middle <= right:
            if nums[middle] == 0:
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
        return nums


print(Solution().sortColors([2, 0, 1]))
