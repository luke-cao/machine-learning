class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in parentheses:
                stack.append(i)
            else:
                if len(stack) == 0 or parentheses[stack.pop()] != i:
                    return False
        return len(stack) == 0
