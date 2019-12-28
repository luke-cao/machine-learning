from typing import List
import heapq


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones_reverse = [-s for s in stones]
#         heapq.heapify(stones_reverse)
#         result = 0
#         while len(stones_reverse) > 0:
#             try:
#                 y = -heapq.heappop(stones_reverse)
#                 x = -heapq.heappop(stones_reverse)
#                 result = y - x
#                 if result > 0:
#                     heapq.heappush(stones_reverse, -result)
#             except IndexError:
#                 result = y
#             except:
#                 print('errors obscured!')
#         return result

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x, y = stones.pop(-2), stones.pop(-1)
            if x == y:
                continue
            else:
                self._insert_ascending(stones, y - x)
        return stones[0] if stones else 0

    def _insert_ascending(self, nums: List[int], num: int) -> List[int]:
        if len(nums) == 0:
            nums.append(num)
            return nums
        index = 0
        for index in range(len(nums)):
            if num < nums[index]:
                nums.insert(index, num)
                break
        if index == len(nums) - 1:
            nums.append(num)
        return nums


test_case = [1, 3]
result = Solution().lastStoneWeight(test_case)
# result = Solution().insert_ascending(sorted(test_case), 5)
print(result)
