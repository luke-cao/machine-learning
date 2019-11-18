from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def left_to_right(left, right, top, bottom, continue_flg):
            row = matrix[top]
            res.extend(row[left: right + 1])
            top += 1
            if top > bottom:
                continue_flg = False
            return left, right, top, bottom, continue_flg

        def top_to_bottom(left, right, top, bottom, continue_flg):
            col = list(zip(*matrix))[right]
            res.extend(col[top: bottom + 1])
            right -= 1
            if left > right:
                continue_flg = False
            return left, right, top, bottom, continue_flg

        def right_to_left(left, right, top, bottom, continue_flg):
            row = matrix[bottom]
            res.extend(row[left: right + 1][::-1])
            bottom -= 1
            if top > bottom:
                continue_flg = False
            return left, right, top, bottom, continue_flg

        def bottom_to_top(left, right, top, bottom, continue_flg):
            col = list(zip(*matrix))[left]
            res.extend(col[top: bottom + 1][::-1])
            left += 1
            if left > right:
                continue_flg = False
            return left, right, top, bottom, continue_flg

        res = []
        if not matrix:
            return res
        continue_flg = True
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while continue_flg:
            if continue_flg:
                left, right, top, bottom, continue_flg = left_to_right(left, right, top, bottom, continue_flg)
            if continue_flg:
                left, right, top, bottom, continue_flg = top_to_bottom(left, right, top, bottom, continue_flg)
            if continue_flg:
                left, right, top, bottom, continue_flg = right_to_left(left, right, top, bottom, continue_flg)
            if continue_flg:
                left, right, top, bottom, continue_flg = bottom_to_top(left, right, top, bottom, continue_flg)
        return res


input = []
print(Solution().spiralOrder(input))