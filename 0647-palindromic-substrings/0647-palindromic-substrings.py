class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[0 for i in range(len(s))]for j in range(len(s))]
        ans=0
        for i in range(len(s)):
            ans+=1
            dp[i][i]=1
        for length in range(2,len(s)+1):
            for low in range(len(s)-length+1):
                high=low+length-1
                if s[low]==s[high]:
                    if high<low+3:
                        dp[low][high]=1
                        ans+=1
                    else:
                        if dp[low+1][high-1]==1:
                            dp[low][high]=1
                            ans+=1
        return ans
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        