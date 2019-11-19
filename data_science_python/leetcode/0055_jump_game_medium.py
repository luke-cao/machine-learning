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
        curr_max_length, length = 0, len(nums) - 1
        for i, v in enumerate(nums):
            if curr_max_length < i:
                return False
            curr_max_length = max(curr_max_length, i + v)
            if curr_max_length >= length:
                return True
        return False


# input = [2,3,1,1,4]
input = [3,2,1,0,4]
# input = [0]
print(Solution().canJump(input))