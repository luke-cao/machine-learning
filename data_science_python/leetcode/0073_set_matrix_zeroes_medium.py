from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # find out zero's coordinate
        coordinates = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    coordinates.append((i, j))
        # set row to zero
        for coordinate in coordinates:
            self.set_zeros_row(matrix, coordinate[0])
            self.set_zeros_col(matrix, coordinate[1])
        # set column to zero

    def set_zeros_row(self, matrix, row):
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    def set_zeros_col(self, matrix, col):
        for row in range(len(matrix)):
            matrix[row][col] = 0


matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Solution().setZeroes(matrix)
print(*matrix, sep='\n')