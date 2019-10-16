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

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    index, cnt = i, 1
        return nums[index]



print(Solution().majorityElement([2,2,1,1,1,1, 2,2]))