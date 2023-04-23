class Solution:
    def helper(self,s,k,i,dp):
        if dp[i]:
            return dp[i]
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        count=0
        for end in range(i,len(s)):
            curr=s[i:end+1]
            if int(curr)>k:
                break
            count+=self.helper(s,k,end+1,dp)
        dp[i]=count%1000000007
        return count
        
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)
        return self.helper(s,k,0,dp)%(10 ** 9 + 7)
    