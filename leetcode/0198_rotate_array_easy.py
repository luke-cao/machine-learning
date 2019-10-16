from typing import List

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= len(nums)
#         for _ in range(k):
#             item = nums.pop()
#             nums.insert(0, item)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]


mylist = [1,2,3,4,5,6,7]
print(Solution().rotate(mylist, 3))
print(mylist)