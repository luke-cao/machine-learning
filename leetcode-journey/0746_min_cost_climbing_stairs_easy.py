from typing import List
from math import inf


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = None, None
        for step, step_cost in enumerate(cost):
            if step == 0:
                prev = cost[step]
                continue
            elif step == 1:
                curr = cost[step]
                continue

            prev, curr = curr, min(step_cost + prev, step_cost + curr)
        return prev if prev < curr else curr

cost = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost2))
