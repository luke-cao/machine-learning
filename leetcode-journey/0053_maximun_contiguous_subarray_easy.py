import json
from typing import List
import numpy as np
from math import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max, local_max = -inf, -inf
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)
        return global_max


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6


