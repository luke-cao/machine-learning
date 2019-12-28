from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back_track(nums, subset=[]):
            if len(nums) == 0:
                ret.append(subset)
                return
            back_track(nums[1:], subset + [nums[0]])
            back_track(nums[1:], subset)

        ret = []
        back_track(nums)
        return ret


print(Solution().subsets([1, 2, 3]))