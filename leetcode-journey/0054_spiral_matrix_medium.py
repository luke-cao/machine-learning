from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def left_to_right():
            nonlocal top, continue_flg
            row = matrix[top]
            res.extend(row[left: right + 1])
            top += 1
            if top > bottom:
                continue_flg = False

        def top_to_bottom():
            nonlocal right, continue_flg
            col = list(zip(*matrix))[right]
            res.extend(col[top: bottom + 1])
            right -= 1
            if left > right:
                continue_flg = False

        def right_to_left():
            nonlocal bottom, continue_flg
            row = matrix[bottom]
            res.extend(row[left: right + 1][::-1])
            bottom -= 1
            if top > bottom:
                continue_flg = False

        def bottom_to_top():
            nonlocal left, continue_flg
            col = list(zip(*matrix))[left]
            res.extend(col[top: bottom + 1][::-1])
            left += 1
            if left > right:
                continue_flg = False

        res = []
        if not matrix:
            return res
        continue_flg = True
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while continue_flg:
            if continue_flg:
                left_to_right()
            if continue_flg:
                top_to_bottom()
            if continue_flg:
                right_to_left()
            if continue_flg:
                bottom_to_top()
        return res


input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(input))
