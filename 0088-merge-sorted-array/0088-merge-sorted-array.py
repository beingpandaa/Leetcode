class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        while j >= 0 and i>=0 :
            if nums2[j]>nums1[i]:
                nums1[i+j+1] = nums2[j]
                j-=1
            else:
                nums1[i+j+1] = nums1[i]
                i-=1
        while j >=0:
            nums1[j]=nums2[j]
            j-=1
        return nums1