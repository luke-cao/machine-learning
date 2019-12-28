class Solution:
    def isHappy(self, n: int) -> bool:
        """
        maybe there is a cycle
        :param n:
        :return:
        """
        seen = set()
        while n != 1:
            seen.add(n)
            m = 0
            for digit in str(n):
                m += int(digit) ** 2
            n = m
            if n in seen:
                return False
        return True


print(Solution().isHappy(18))
