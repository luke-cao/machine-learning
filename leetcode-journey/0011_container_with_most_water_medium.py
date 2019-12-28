from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            if curr_area > area:
                area = curr_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


# time limit
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for left in range(len(height) - 1):
            for right in range(1, len(height)):
                if (right - left) * min(height[left], height[right]) > area:
                    area = (right - left) * min(height[left], height[right])
        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(Solution().maxArea([1,2,1]))  # 2
print(Solution().maxArea([1,2,4,3]))  # 4
