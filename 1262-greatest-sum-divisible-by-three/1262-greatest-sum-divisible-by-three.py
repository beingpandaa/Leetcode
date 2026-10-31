class Solution:
    def dfs(self,nums,dp,curr=0,i=0):
        if (i,curr) not in dp:
            if i==len(nums):
                if not curr: return 0
                return float("-inf")
            
            dp[(i,curr)] = max(self.dfs(nums,dp,curr,i+1),nums[i]+self.dfs(nums,dp,(curr+nums[i])%3,i+1))
        return dp[(i,curr)]
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp={}
        return self.dfs(nums,dp)