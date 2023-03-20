class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[-1 for i in range(n+1)]
        for i in range(n+1):
            if i==0 or i==1:
                dp[i]=i
            if i&1==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=1+dp[i-1]
        return dp