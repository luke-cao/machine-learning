from typing import List


# time complexity is not o(log(n)), is actually o(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or nums[-1] < target < nums[0]:
            return -1
        elif target >= nums[0]:
            # search from beginning until reach maximum, if not found, return -1
            for i in range(len(nums)):
                if i > 0 and nums[i] < nums[i - 1]:
                    break
                if nums[i] == target:
                    return i
        else:
            # search from the end until reach minimum, if not found return - 1
            for i in range(len(nums) - 1, 0, -1):
                if i < len(nums) - 2 and nums[i] > nums[i + 1]:
                    break
                if nums[i] == target:
                    return i
        return -1


# time complexity is o(log(n)), need use binary midpoint search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                if nums[start] <= target and nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            elif nums[mid] > target:
                if target <= nums[end] and nums[end] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


input = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(input, target))
# print(Solution().find_value_in_sorted_list([1, 7], 7))