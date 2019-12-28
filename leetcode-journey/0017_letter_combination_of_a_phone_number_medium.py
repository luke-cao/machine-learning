from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         num_to_alphas = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#         result = ['']
#         for digit in digits:
#             new_result = []
#             for i in range(len(result)):
#                 for letter in num_to_alphas[digit]:
#                     new_result.append(result[i] + letter)
#             result = new_result
#         return result


# backtracking algorithm
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

        def backtrack(combination, digits):
            if len(digits) == 0:
                result.append(combination)
            else:
                for letter in phone[digits[0]]:
                    backtrack(combination + letter, digits[1:])

        result = []
        if digits:
            backtrack('', digits)
        return result


input = '23'
result = Solution().letterCombinations(input)
# assert result == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 'Wrong'
