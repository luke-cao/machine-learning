from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find out first target
        ret = [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid > 0 and nums[mid - 1] != target or mid == 0):
                ret[0] = mid
                break
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if ret[0] == -1:
            return ret

        left, right = ret[0], len(nums) - 1
        # find out last target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid < len(nums) - 1 and nums[mid + 1] != target or mid == len(nums) - 1):
                ret[1] = mid
                break
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return ret


nums = [2, 2]
target = 2
print(Solution().searchRange(nums, target))
