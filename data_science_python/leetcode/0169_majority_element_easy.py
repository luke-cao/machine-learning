from typing import List
from collections import Counter

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counter = Counter(nums)
#         return counter.most_common(1)[0][0]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         halfline = len(nums) / 2
#         counter = {}
#         for i in nums:
#             if i in counter:
#                 counter[i] = counter[i] + 1
#             else:
#                 counter[i] = 1
#             if counter.get(i) > halfline:
#                 return i
#         return 'No Majority'

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """
#         the majority element appears more than half of total number
#         :param nums:
#         :return:
#         """
#         index, cnt = 0, 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[index]:
#                 cnt += 1
#             else:
#                 cnt -= 1
#                 if cnt == 0:
#                     index, cnt = i, 1
#         return nums[index]


class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)




print(Solution().majorityElement([2,2,1,1,1,2,2]))