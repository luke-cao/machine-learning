from typing import List

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         counter1 = dict()
#         counter2 = dict()
#         for num in nums1:
#             if num in counter1:
#                 counter1[num] += 1
#             else:
#                 counter1[num] = 1
#         for num in nums2:
#             if num in counter2:
#                 counter2[num] += 1
#             else:
#                 counter2[num] = 1
#         for num, count in counter1.items():
#             if num in counter2:
#                 counter1[num] = min(count, counter2[num])
#             else:
#                 counter1[num] = 0
#         ret = list()
#         for num, count in counter1.items():
#             ret.extend([num] * count)
#         return ret


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        lookup = dict()
        for num in nums1:
            if num in lookup:
                lookup[num] += lookup[num]
            else:
                lookup[num] = 1
        ret = []
        for num in nums2:
            if lookup.get(num, 0):
                ret.append(num)
                lookup[num] -= 1
        return ret


nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))