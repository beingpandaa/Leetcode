class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        def dfs(n,dp):
            if n==1 or n==2:return n
            if dp[n-1]==-1:
                dp[n-1]=dfs(n-1,dp)
            if dp[n-2]==-1:
                dp[n-2]=dfs(n-2,dp)
            return dp[n-1]+dp[n-2]
        dp=[-1 for i in range(n)]
        return dfs(n,dp)