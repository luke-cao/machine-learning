import json
from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        mem = [-1 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            for c in coins:
                if i - c > 0 and mem[i - c] > 0:
                    min_coin_amt = mem[i - c] + 1
                    if mem[i] < 0 or min_coin_amt < mem[i]:
                        mem[i] = min_coin_amt
                elif i - c == 0:
                    mem[i] = 1
        return mem[-1]


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            coins = stringToIntegerList(line);
            line = next(lines)
            amount = int(line);

            ret = Solution().coinChange(coins, amount)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()