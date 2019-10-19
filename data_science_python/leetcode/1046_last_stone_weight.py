from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_reverse = [-s for s in stones]
        heapq.heapify(stones_reverse)
        result = 0
        while len(stones_reverse) > 0:
            try:
                y = -heapq.heappop(stones_reverse)
                x = -heapq.heappop(stones_reverse)
                result = y - x
                if result > 0:
                    heapq.heappush(stones_reverse, -result)
            except IndexError:
                result = y
            except:
                print('errors obscured!')
        return result


test_case = [2, 7, 4, 1, 8, 1]
result = Solution().lastStoneWeight(test_case)
print(result)
