class NumArray(object):

    def __init__(self, nums):
        self.prefix_sums = [0] * (len(nums) + 1)
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            self.prefix_sums[i + 1] = current_sum

    def sumRange(self, left, right):
        return self.prefix_sums[right + 1] - self.prefix_sums[left]