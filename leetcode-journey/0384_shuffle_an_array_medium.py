from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        nums_copy = self.nums.copy()
        while nums_copy:
            index = random.randrange(0, len(nums_copy))  # random.randrange and random.randint
            res.append(nums_copy.pop(index))
        return res

# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
# param_1 = obj.reset()
# print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)