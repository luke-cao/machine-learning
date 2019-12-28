class Solution:
    def isValid(self, s: str) -> bool:
        """
        the parentheses are first in first out
        :param s:
        :return:
        """
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in parentheses:
                stack.append(i)
            else:
                if len(stack) == 0 or parentheses[stack.pop()] != i:
                    return False
        return len(stack) == 0
