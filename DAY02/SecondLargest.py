class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        largest = -1
        second_largest = -1
        for i in range(len(arr)):
            x = arr[i]
            if x > largest:
                second_largest = largest
                largest = x
            elif x > second_largest and x != largest:
                second_largest = x
        return second_largest