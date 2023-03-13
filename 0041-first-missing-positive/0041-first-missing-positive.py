class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_missing=len(nums)+1
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if index>=0 and index<len(nums):
                if nums[index]==0:
                    nums[index]=-(index+1)
                else:
                    nums[index]=-abs(nums[index])
                
        for i in range(1,max_missing):
            index=i-1
            if nums[index]>=0:return i
        return max_missing
            
            