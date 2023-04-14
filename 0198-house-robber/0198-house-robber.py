class Solution:
    # def helper(self,nums,i,dp):
    #     if i>=len(nums):return 0
    #     if dp[i]!=-1:return dp[i]
    #     ans1=nums[i]+self.helper(nums,i+2,dp)
    #     ans2=self.helper(nums,i+1,dp)
    #     dp[i]=max(ans1,ans2)
    #     return dp[i]
    def rob(self, nums: List[int]) -> int:
        # dp=[-1 for i in range(len(nums))]
        # return self.helper(nums,0,dp)
        dp=[0 for i in range(len(nums)+2)]
        for i in range(len(nums)-1,-1,-1):
            dp[i]=max(nums[i]+dp[i+2],dp[i+1])
        return dp[0]