from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        curr_max = 0
        last_max = 0
        for num in nums:
            last_last_max, last_max = last_max, curr_max
            curr_max = max(num + last_last_max, last_max)
        return curr_max



print(Solution().rob([2, 7, 9, 3, 1]))


