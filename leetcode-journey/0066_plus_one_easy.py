from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = list(map(str, digits))
#         digits = int(''.join(digits))
#         digits += 1
#         digits = list(str(digits))
#         return list(map(int, digits))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            if len(digits) == 1:
                digits = [0] + digits
            return self.plusOne(digits[:-1]) + [0]
        else:
            return digits


print(Solution().plusOne([1, 2, 3]))
