from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_idx = defaultdict(list)
        for idx, value in enumerate(nums):
            num_idx[value].append(idx)
        for idxs in num_idx.values():
            if len(idxs) == 1:
                continue
            for i in range(len(idxs) - 1):
                if abs(idxs[i] - idxs[i + 1]) <= k:
                    return True
        return False


# Time limit exceeded
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for idx_left, value_left in enumerate(nums):
            for idx_right in range(idx_left + 1, len(nums)):
                value_right = nums[idx_right]
                if value_left == value_right and abs(idx_left - idx_right) <= k:
                    return True
        return False


class Solution3:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for idx, num in enumerate(nums):
            if num in lookup and abs(lookup[num] - idx) <= k:
                return True
            else:
                lookup[num] = idx
        return False


nums = [1, 2, 3, 1]
k = 3
assert Solution3().containsNearbyDuplicate(nums, k) == True, Solution().containsNearbyDuplicate(nums, k)

nums = [1,0,1,1]
k = 1
assert Solution3().containsNearbyDuplicate(nums, k) == True, Solution().containsNearbyDuplicate(nums, k)

nums = [1,2,3,1,2,3]
k = 2
assert Solution3().containsNearbyDuplicate(nums, k) == False, Solution().containsNearbyDuplicate(nums, k)
