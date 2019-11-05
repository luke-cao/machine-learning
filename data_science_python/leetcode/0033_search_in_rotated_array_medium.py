from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or nums[-1] < target < nums[0]:
            return -1
        elif target >= nums[0]:
            # search from beginning until reach maximum, if not found, return -1
            for i in range(len(nums)):
                if i > 0 and nums[i] < nums[i - 1]:
                    break
                if nums[i] == target:
                    return i
        else:
            # search from the end until reach minimum, if not found return - 1
            for i in range(len(nums) - 1, 0, -1):
                if i < len(nums) - 2 and nums[i] > nums[i + 1]:
                    break
                if nums[i] == target:
                    return i
        return -1


input = []
target = 3
print(Solution().search(input, target))
