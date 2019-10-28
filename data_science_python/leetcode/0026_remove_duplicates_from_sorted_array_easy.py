from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1


input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
count = Solution().removeDuplicates(input)
print(count)
print(input)
print(input[:count])
