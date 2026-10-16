class Solution:
  def intersection(self, nums1,nums2):
    set1 = set(nums1)
    result_set = set()
    for num in nums2:
      if num in set1:
        result_set.add(num)
    result = []
    for num in result_set:
      result.append(num)
    return result