class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
                
        i=len(nums)-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i-=1
        reverse(nums,i,len(nums)-1)
        if i!=0:
            index=i-1
            for i in range(i,len(nums)):
                if nums[i]>nums[index]:
                    nums[index],nums[i]=nums[i],nums[index]
                    break
            
        