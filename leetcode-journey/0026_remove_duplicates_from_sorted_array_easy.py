from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]
        return idx + 1


input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
count = Solution().removeDuplicates(input)
print(count)
print(input)
print(input[:count])
