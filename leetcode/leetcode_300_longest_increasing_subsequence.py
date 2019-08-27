import json
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_lens = [1 for _ in range(len(nums))]
        max_ret = 1
        for i in range(1, len(nums)):
            cur_max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if max_lens[j] + 1 > cur_max_len:
                        cur_max_len = max_lens[j] + 1
            if cur_max_len > max_ret:
                max_ret = cur_max_len
            max_lens[i] = cur_max_len
        return max_ret



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
            nums = stringToIntegerList(line);

            ret = Solution().lengthOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

"""
[10,9,2,5,3,7,101,18]
4
"""