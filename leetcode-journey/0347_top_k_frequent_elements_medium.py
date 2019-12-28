from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_k = counter.most_common(k)
        return [item[0] for item in counter_k]


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         return heapq.nlargest(k, count.keys(), key=count.get)


print(Solution().topKFrequent([1,1,1,2,2,3, 3, 3, 3], 2))