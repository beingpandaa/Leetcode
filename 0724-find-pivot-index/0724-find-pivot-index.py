class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
         # nums = [1,7,3,6,5,6]
         #        1  8 11 17 22 28
        for i in range(1,len(nums)):nums[i]+=nums[i-1]
        if nums[len(nums)-1]-nums[0]==0:return 0
        for i in range(1,len(nums)):
            if nums[len(nums)-1]-nums[i]==nums[i-1]:return i
        return -1