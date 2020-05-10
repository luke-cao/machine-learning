from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in dict:
                dict[nums[i]] = i
            else:
                return [dict[complement], i]


# print(Solution().twoSum([2, 7, 11, 15], 9))
assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1], Solution().twoSum([2, 7, 11, 15], 9)
assert Solution().twoSum([3, 3], 6) == [0, 1]