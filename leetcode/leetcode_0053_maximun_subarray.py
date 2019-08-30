import json
from typing import List
import numpy as np

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_ret = nums[0]
        cur_max = last_max = nums[0]
        for i in range(1, len(nums)):
            if last_max + nums[i] < nums[i]:
                cur_max = nums[i]
            else:
                cur_max = last_max + nums[i]
            if cur_max > max_ret:
                max_ret = cur_max
            last_max = cur_max
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

            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

"""
[-2,1,-3,4,-1,2,1,-5,4]
6
"""
