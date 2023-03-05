class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        curr_prof=0
        buy_at=prices[0]
        for i in range(len(prices)):
            if prices[i]>buy_at:
                profit+=prices[i]-buy_at 
            buy_at=prices[i]         
        return profit
                