from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1 in range(len(numbers)):
            left, right = idx1 + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[idx1] + numbers[mid] < target:
                    left = mid + 1
                elif numbers[idx1] + numbers[mid] == target:
                    return [idx1 + 1, mid + 1]
                else:
                    right  = mid - 1
        return None


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            sum_ = numbers[start] + numbers[end]
            if sum_ < target:
                start += 1
            elif sum_ > target:
                end -= 1
            else:
                return [start + 1, end - 1]

