class Solution(object):
    def sortedSquares(self, nums):
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
        return res