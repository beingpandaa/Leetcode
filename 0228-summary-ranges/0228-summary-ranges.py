class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        op=[]
        i=0
        while i<len(nums):
            s=str(nums[i])
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            if str(nums[i])!=s:s=s+'->'+str(nums[i])   
            op.append(s)
            i+=1
        return op
            
            
            