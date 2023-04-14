class Solution:
    def itr(self,s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
    def helper(self,s,i,j,d):
        if i>j:return 0
        if i==j:return 1
        if (i,j) in d:return d[(i,j)]
        if s[i]==s[j]:
            d[(i,j)]=2+self.helper(s,i+1,j-1,d)
            return d[(i,j)]
        else:
            ans1=self.helper(s,i+1,j,d)
            ans2=self.helper(s,i,j-1,d)
            d[(i,j)]= max(ans1,ans2)
            return d[(i,j)]
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.itr(s)
        # return self.helper(s,0,len(s)-1,d={})