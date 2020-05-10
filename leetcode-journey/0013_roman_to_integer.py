class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        p = None
        for c in s:
            total += roman_to_int_dict[c]
            if p and roman_to_int_dict[c] > roman_to_int_dict[p]:
                total -= 2 * roman_to_int_dict[p]
            p = c
        return total


assert Solution().romanToInt('DCXXI') == 621
assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('IV') == 4
assert Solution().romanToInt('LVIII') == 58

