class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if len(s) == 0:
            return 0
        sign = False
        if s[0] == '-':
            sign = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif not s[0].isdigit():
            return 0
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        if i == 0:
            return 0
        s = -int(s[:i]) if sign else int(s[:i])
        if s < -2 ** 31:
            return -2 ** 31
        elif s > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return s


print(Solution().myAtoi("42"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))