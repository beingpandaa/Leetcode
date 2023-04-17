class Solution:
    def helper(self,d,tar,words,i,k,dp):
        if i==len(tar):return 1
        if k==len(words[0]):return 0
        if dp[i][k+1]==-1:dp[i][k+1]=self.helper(d,tar,words,i,k+1,dp)
        ans1=dp[i][k+1]
        ans2=0
        if (k,tar[i]) in d:
            if dp[i+1][k+1]==-1:dp[i+1][k+1]=self.helper(d,tar,words,i+1,k+1,dp)
            ans2=d[(k,tar[i])]*dp[i+1][k+1]
        return ans1+ans2
    def numWays(self, words: List[str], tar: str) -> int:
        dp=[[-1 for k in range(len(words[0])+1)] for i in range(len(tar)+1)]
        d={}
        for i in range(len(words)):
            for j in range(len(words[0])):
                d[(j,words[i][j])]=d.get((j,words[i][j]),0)+1
        return self.helper(d,tar,words,0,0,dp)%1000000007