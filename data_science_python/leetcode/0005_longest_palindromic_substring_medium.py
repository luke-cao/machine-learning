class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)):
            p = self.get_longest_palindrome(s, i, i)
            if len(p) > len(palindrome):
                palindrome = p

            p = self.get_longest_palindrome(s, i, i + 1)
            if len(p) > len(palindrome):
                palindrome = p
        return palindrome

    def get_longest_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return s[j + 1: k]


print(Solution().longestPalindrome('cbbd'))

