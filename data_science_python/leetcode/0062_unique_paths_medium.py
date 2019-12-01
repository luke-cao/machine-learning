# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def move(x, y):
#             nonlocal unique_paths_count
#
#             if x == m - 1 and y == n - 1:
#                 unique_paths_count += 1
#                 return
#             elif x >= m or y >= n:
#                 return
#
#             # go right
#             move(x + 1, y)
#             # go down
#             move(x, y + 1)
#
#         unique_paths_count = 0
#         move(0, 0)
#         return unique_paths_count

from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m - 1 + n - 1
        down = n - 1
        return int(factorial(total) / factorial(total - down) / factorial(down))


print(Solution().uniquePaths(57, 2))