from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_nums1 = 0
        idx_nums2 = 0
        for idx_nums1 in range(m):
            if idx_nums2 == n:
                break
            if nums2[idx_nums2] >= nums1[m - 1 + idx_nums2]:
                break
            if nums2[idx_nums2] < nums1[idx_nums1 + idx_nums2]:
                nums1.pop()
                nums1.insert(idx_nums1 + idx_nums2, nums2[idx_nums2])
                idx_nums2 += 1
        nums1[idx_nums1 + idx_nums2 + 1:] = nums2[idx_nums2:]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
