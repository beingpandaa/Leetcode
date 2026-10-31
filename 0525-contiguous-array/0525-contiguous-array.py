class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        temp = 0 
        ans = 0
        for i in range(len(nums)):
            
            if nums[i] ==1: temp+=1
            else:temp-=1
           
            if temp==0: ans = i+1
            elif temp in d: ans = max(ans,i-d[temp])
            else:d[temp] = i
        return ans