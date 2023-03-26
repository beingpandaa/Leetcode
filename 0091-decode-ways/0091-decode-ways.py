class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        
        
        def decode(s,i,dp):
            if i>=len(s):return 1
            if s[i]=='0':return 0
            if dp[i+1]==-1:dp[i+1]=decode(s,i+1,dp)
            ans1=dp[i+1]
            ans2=0
            if i<len(s)-1 and int(s[i:i+2])<27:
                if dp[i+2]==-1:dp[i+2]=decode(s,i+2,dp)
                ans2=dp[i+2]
            return ans1+ans2
        dp=[-1 for i in range (len(s)+1)]
        return decode(s,0,dp)
        