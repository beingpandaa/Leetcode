class Solution:
    def helper(self,prices,i,buy,fee,dp):
        if i==len(prices):
            return 0
        
        if not buy:
            if dp[i+1][1]==-1:dp[i+1][1]=self.helper(prices,i+1,1,fee,dp)
            prof1=-prices[i]+dp[i+1][1]
            if dp[i+1][0]==-1:dp[i+1][0]=self.helper(prices,i+1,0,fee,dp)
            prof2=dp[i+1][0]
        else:
            if dp[i+1][0]==-1:dp[i+1][0]=self.helper(prices,i+1,0,fee,dp)
            prof1=prices[i]+dp[i+1][0]-fee
            if dp[i+1][1]==-1:dp[i+1][1]=self.helper(prices,i+1,1,fee,dp)
            prof2=dp[i+1][1]
        return max(prof1,prof2)
        
        
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp=[[-1 for i in range (2)] for j in range(len(prices)+1)]
        return self.helper(prices,0,0,fee,dp)
            
            
            
                
            