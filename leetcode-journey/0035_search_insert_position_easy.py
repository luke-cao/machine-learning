from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[left]:
                if mid - left == 1:
                    return mid
                left = mid + 1
            else:
                if right - mid == 1:
                    return right
                right = mid - 1


input = [1, 3, 5, 6]
target = 4
print(Solution().searchInsert(input, target))