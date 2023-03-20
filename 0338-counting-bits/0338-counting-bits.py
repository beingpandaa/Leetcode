class Solution:
    def countBits(self, n: int) -> List[int]:
        # def dfs(n,dp):
        #     if n==1:return 1
        #     if dp[n]==-1:
        #         if n&1==0:
        #             dp[n]=dfs(n>>1,dp)
        #         else:
        #             dp[n]=1+dfs(n-1,dp)
        #     return dp[n]
        dp=[-1 for i in range(n+1)]
        for i in range(n+1):
            if i==0 or i==1:
                dp[i]=i
            if i&1==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=1+dp[i-1]
        return dp