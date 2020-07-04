class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        while n:
            result += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) // 26
        return result[::-1]