from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [str(i) for i in range(n + 1)]
        multiplier = 1
        while 3 * multiplier <= n:
            ret[3 * multiplier] = 'Fizz'
            multiplier += 1
        multiplier = 1
        while 5 * multiplier <= n:
            if ret[5 * multiplier] == 'Fizz':
                ret[5 * multiplier] = 'FizzBuzz'
            else:
                ret[5 * multiplier] = 'Buzz'
            multiplier += 1
        return ret[1:]


print(Solution().fizzBuzz(15))