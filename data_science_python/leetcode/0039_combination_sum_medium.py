from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def back_track(target, start, combination):
            if target < 0:
                return
            elif target == 0:
                res.append(combination)
            else:
                for i in range(start, len(candidates)):
                    back_track(target - candidates[i], i, combination + [candidates[i]])

        back_track(target, 0, [])
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
