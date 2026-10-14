class Solution:
    def countFreq(self, arr):
        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        result = []
        visited = set()
        for num in arr:
            if num not in visited:
                result.append([num, freq_map[num]])
                visited.add(num)

        return result