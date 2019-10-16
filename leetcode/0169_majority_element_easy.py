from typing import List
from collections import Counter

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counter = Counter(nums)
#         return counter.most_common(1)[0][0]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halfline = len(nums) // 2
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] = counter[i] + 1
            else:
                counter[i] = 1
            if counter.get(i) > halfline:
                return i
        return 'No Majority'



print(Solution().majorityElement([1]))