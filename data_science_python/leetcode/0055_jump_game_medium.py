from typing import List

# backtracking time limit exceed
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in reversed(range(len(nums) - 1)):
            length = len(nums) - 1 - i
            if nums[i] >= length:
                if i == 0:
                    return True
                flg = self.canJump(nums[:i + 1])
                if flg:
                    return True
        return False


# dynamic programming
class Solution:
    def canJump(self, nums):
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x)


input = [2,3,1,1,4]
# input = [3,2,1,0,4]
# input = [0]
print(Solution().canJump(input))