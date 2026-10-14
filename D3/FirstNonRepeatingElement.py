class Solution:
    def firstNonRepeating(self, arr):
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            
        for num in arr:
            if counts[num] == 1:
                return num
                
        return 0