class Solution:
    def divisorGame(self, n: int) -> bool:
        
        
        def dfs(n,dp):
            if n<=1:return False
            for i in range(1,n):
                if n%i==0:
                    if dp[n-i]==-1:
                        dp[n-i]=dfs(n-i,dp)
                    if dp[n-i]==False:return True
            return False
        dp=[-1 for i in range(n)]
        return dfs(n,dp)