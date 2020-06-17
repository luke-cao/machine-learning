from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # sort the list
        nums.sort()
        # check the missing numbers
        results = []
        results.extend(list(range(1, nums[0])))
        for i in range(len(nums) - 1):
            missing_nums = list(range(nums[i] + 1, nums[i + 1]))
            if missing_nums:
                results.extend(missing_nums)
        results.extend(list(range(nums[-1] + 1, len(nums) + 1)))
        return results


actual_result = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
assert actual_result == [5, 6], actual_result

actual_result = Solution().findDisappearedNumbers([1, 1])
assert actual_result == [2], actual_result

actual_result = Solution().findDisappearedNumbers([2, 2])
assert actual_result == [1], actual_result
