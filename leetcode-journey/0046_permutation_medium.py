from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back_track(ret: List[int], nums: List[int]):
            if len(nums) == 0:
                ans.append(ret)
            for i in range(len(nums)):
                back_track(ret + [nums[i]], nums[:i] + nums[i + 1:])

        ans = []
        back_track([], nums)
        return ans


print(Solution().permute([1, 2, 3]))