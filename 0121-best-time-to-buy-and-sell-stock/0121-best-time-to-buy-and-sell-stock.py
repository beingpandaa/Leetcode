class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = 999999
        for ele in prices:
            profit = max(profit,ele-curr_min)
            curr_min = min(curr_min,ele)
        return profit

            
                

