class Solution:
    def largest(self, arr: list[int]) -> int:
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
        return max_val