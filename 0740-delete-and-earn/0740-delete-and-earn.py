class Solution:
    def helper(self,nums,i,d,deepee):
        if i==len(nums)-1:return nums[i]*d[nums[i]]
        if i==len(nums):return 0
        
        ans1=nums[i]*d[nums[i]]
        if nums[i+1]==nums[i]+1:
            
            if deepee[i+2]==-1:deepee[i+2]=self.helper(nums,i+2,d,deepee)
            if deepee[i+1]==-1:deepee[i+1]=self.helper(nums,i+1,d,deepee)
            
            
            ans1+=deepee[i+2]
            ans2=deepee[i+1]
            
            return max(ans1,ans2)
        else:
            if deepee[i+1]==-1:deepee[i+1]=self.helper(nums,i+1,d,deepee)
            ans1+=deepee[i+1]
        
            return ans1
        
        
    def deleteAndEarn(self, nums: List[int]) -> int:
        d=Counter(nums)
        nums=sorted(list(set(nums)))
        deepee=[-1 for i in range(len(nums)+1)]
        return self.helper(nums,0,d,deepee)