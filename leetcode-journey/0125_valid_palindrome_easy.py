import re


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub(r'[^a-zA-Z0-9]+', '', s)
#         s = s.lower()
#         return s[::1] == s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        isalnum()
        linear complexity, no extra memory, ignore case
        :param s:
        :return:
        """
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
