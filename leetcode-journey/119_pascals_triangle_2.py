from typing import List
from math import factorial


# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         result = [None] * (rowIndex + 1)
#         for i in range(rowIndex + 1):
#             result[i] = round(factorial(rowIndex) / factorial(i) / factorial(rowIndex - i))
#         return result


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                result[j] = result[j - 1] + result[j]
        return result



assert Solution().getRow(3) == [1,3,3,1]
