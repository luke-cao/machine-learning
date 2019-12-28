from typing import List
import collections


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        prev_idx = 0
        for curr_idx in range(1, len(intervals)):
            if intervals[curr_idx][0] <= intervals[prev_idx][1]:
                intervals[prev_idx][1] = max(intervals[prev_idx][1], intervals[curr_idx][1])
                intervals[curr_idx] = None
            else:
                prev_idx = curr_idx
        return [i for i in intervals if i]



input = [[1,3],[2,6],[8,10],[15,18]]
input2 = [[1,4],[4,5]]
print(Solution().merge(input))
print(Solution().merge(input2))