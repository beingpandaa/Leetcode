class Solution:
    def helper(self,prices,i,buy,dp):
        if i==len(prices):
            return 0
        
        if not buy:
            if dp[i+1][1]==-1:dp[i+1][1]=self.helper(prices,i+1,1,dp)
            prof1=-prices[i]+dp[i+1][1]
            if dp[i+1][0]==-1:dp[i+1][0]=self.helper(prices,i+1,0,dp)
            prof2=dp[i+1][0]
        else:
            if dp[i+1][0]==-1:dp[i+1][0]=self.helper(prices,i+1,0,dp)
            prof1=prices[i]+dp[i+1][0]
            if dp[i+1][1]==-1:dp[i+1][1]=self.helper(prices,i+1,1,dp)
            prof2=dp[i+1][1]
        return max(prof1,prof2)
            
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # curr_prof=0
        # buy_at=prices[0]
        # for i in range(len(prices)):
        #     if prices[i]>buy_at:
        #         profit+=prices[i]-buy_at 
        #     buy_at=prices[i]         
        # return profit
        dp=[[-1 for i in range (2)] for j in range(len(prices)+1)]
        return self.helper(prices,0,0,dp)
                