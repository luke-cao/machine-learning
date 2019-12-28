from typing import List


# class Solution:
# #     def moveZeroes(self, nums: List[int]) -> None:
# #         """
# #         Do not return anything, modify nums in-place instead.
# #         """
# #         zero_ptr, n_zero_ptr = 0, 0
# #         num_len = len(nums)
# #         while zero_ptr < num_len and n_zero_ptr < num_len:
# #             # find out the next zero item
# #             while zero_ptr < num_len and nums[zero_ptr] != 0:
# #                 zero_ptr += 1
# #             # find out the next non-zero item
# #             while n_zero_ptr < num_len and nums[n_zero_ptr] == 0:
# #                 n_zero_ptr += 1
# #             if n_zero_ptr < zero_ptr:
# #                 n_zero_ptr += 1
# #                 continue
# #             if zero_ptr >= num_len or n_zero_ptr >= num_len:
# #                 return
# #             if nums[zero_ptr] == 0 and nums[n_zero_ptr] != 0:
# #                 nums[zero_ptr], nums[n_zero_ptr] = nums[n_zero_ptr], nums[zero_ptr]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0


input = [1, 0]
Solution().moveZeroes(input)
print(input)
