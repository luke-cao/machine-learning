from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = [[1 for j in range(i + 1)] for i in range(numRows)]
        for row in range(2, len(grid)):
            for col in range(1, len(grid[row]) - 1):
                grid[row][col] = grid[row - 1][col - 1] + grid[row - 1][col]
        return grid

print(Solution().generate(5))
