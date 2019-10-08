from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        standard = (r0, c0)
        cells_dict = {}
        for r in range(R):
            for c in range(C):
                cell = (r, c)
                cells_dict[cell] = abs(cell[0] - standard[0]) + abs(cell[1] - standard[1])
        return sorted(cells_dict, key=lambda key: cells_dict[key])


print(Solution().allCellsDistOrder(2, 3, 1, 2))