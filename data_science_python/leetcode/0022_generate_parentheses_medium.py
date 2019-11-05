from typing import List


# backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(stack='', left=0, right=0):
            if len(stack) == 2 * n:
                ans.append(stack)
                return
            if left < n:
                backtrack(stack + '(', left + 1, right)
            if right < left:
                backtrack(stack + ')', left, right + 1)

        backtrack()
        return ans


print(Solution().generateParenthesis(3))