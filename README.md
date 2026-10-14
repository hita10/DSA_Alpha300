1*
Majority ElementApproach:
Iterate through the array to build a frequency map using a plain dictionary. In the same or a subsequent pass, check which element's frequency exceeds n // 2.
Time Complexity: O(n) Space Complexity: O(n)
Edge Case Missed on First Attempt: Handling a single-element array where the count check needs to correctly return the sole element without failing on boundary conditions.
2*
First Non-Repeating Element in ArrayApproach:
Perform a first pass to populate a frequency count dictionary. Perform a second pass over the array to find the first element whose count in the dictionary equals 1.Time Complexity: O(n)
Space Complexity: O(n)
Edge Case Missed on First Attempt: Failing to return -1 or a default indicator when every element in the array has duplicates.
3*
Count Frequencies of Array Elements 
Approach: Initialize an empty dictionary and iterate through the input list, updating the count for each element manually using .get(element, 0) + 1.Time Complexity: O(n)
Space Complexity: O(n)
Edge Case Missed on First Attempt: Handling empty arrays correctly by ensuring the output handles zero-length inputs gracefully.
