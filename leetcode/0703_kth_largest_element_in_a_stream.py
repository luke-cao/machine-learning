from heapq import heapify, heappush, heappop, heappushpop


class KthLargest(object):

    def __init__(self, k: int, nums: list):
        self.k = k
        self.k_flag = True
        if len(nums) >= k:
            self.heap = sorted(nums, reverse=True)[:k]
        else:
            self.heap = nums
            self.k_flag = False
        heapify(self.heap)

    def add(self, val):
        if self.k_flag:
            if val > self.heap[0]:
                heappushpop(self.heap, val)
            return self.heap[0]
        else:
            heappush(self.heap, val)
            if len(self.heap) >= self.k:
                self.k_flag = True
            return None


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

inputs, add_nums = [3, [4, 5, 8, 2]], [3, 5, 10, 9, 4]
kthLargest = KthLargest(*inputs)
for num in add_nums:
    print(kthLargest.add(num))

