class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i,total,dp):
            if i==len(nums):
                if total==target:
                    return 1
                else:
                    return 0
            if dp[i+1][total+nums[i]]==1001:dp[i+1][total+nums[i]]=dfs(i+1,total+nums[i],dp)
            if dp[i+1][total-nums[i]]==1001:dp[i+1][total-nums[i]]=dfs(i+1,total-nums[i],dp)
            
            return dp[i+1][total+nums[i]]+dp[i+1][total-nums[i]]
        dp=[[1001 for i in range(2*sum(nums)+1)]for i in range(len(nums)+1)]
        return dfs(0,0,dp)
            
            