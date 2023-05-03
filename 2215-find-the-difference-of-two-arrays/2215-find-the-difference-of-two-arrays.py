class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s=set(nums1)
        t=set(nums2)
        return [list(s-t),list(t-s)]