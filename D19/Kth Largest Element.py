class Solution(object):
    def findKthLargest(self, nums, k):
        target_index = len(nums) - k
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            pivot_index = left + (right - left) // 2
            final_index = self._partition(nums, left, right, pivot_index)
            
            if final_index == target_index:
                return nums[final_index]
            elif final_index < target_index:
                left = final_index + 1
            else:
                right = final_index - 1
                
        return -1

    def _partition(self, nums, left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
                
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index