from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def make_adjacent_zero(i, j, row_len, col_len):
            grid[i][j] = 0
            # up
            if i > 0 and grid[i - 1][j] == '1':
                make_adjacent_zero(i - 1, j, row_len, col_len)
            # down
            if i < row_len - 1 and grid[i + 1][j] == '1':
                make_adjacent_zero(i + 1, j, row_len, col_len)
            # left
            if j > 0 and grid[i][j - 1] == '1':
                make_adjacent_zero(i, j - 1, row_len, col_len)
            # right
            if j < col_len - 1 and grid[i][j + 1] == '1':
                make_adjacent_zero(i, j + 1, row_len, col_len)

        count = 0
        row_len, col_len = len(grid), len(grid[0]) if len(grid) > 0 else 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    count += 1
                    make_adjacent_zero(i, j, row_len, col_len)
        return count


input = """"""
input = input.split('\n')
input = [list(row) for row in input]
for i in input:
    for j in i:
        print(j, sep='', end='')
    print('\n')
print(Solution().numIslands(input))

