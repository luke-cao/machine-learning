class NumArray:
    def __init__(self, nums: List[int]):
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)