class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        j=0
        total=0
        maxSum=-10000
        while j<len(nums):  
            total+=nums[j]
            maxSum=max(total,maxSum)
            j+=1
            if total<0:
                total=0
                i=j
        return maxSum
            
                
                