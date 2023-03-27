class Solution:
    def helperitr(self,coins,dp):
        for i in range(len(dp)):
            dp[i][0]=0
        for j in range(len(dp[0])):
            dp[len(dp)-1][j]=sys.maxsize
        minVal=sys.maxsize
        for i in range(len(dp)-1,-1,-1):
            for amt in range(len(dp[0])):
                if dp[i][amt]==-1:
                    if amt-coins[i]<0:
                        ans1=sys.maxsize
                    else:
                        ans1=1+dp[i][amt-coins[i]]
                    ans2=dp[i+1][amt]
                    dp[i][amt]=min(ans1,ans2)
                if amt==len(dp[0])-1:minVal=min(minVal,dp[i][amt])
        return minVal
                    
                
                
    def helper(self,coins,i,total,dp):
        if total==0:return 0
        if total<0 or i==len(coins):return sys.maxsize
        
        if total-coins[i]<0:ans1=sys.maxsize
        else:
        
            if dp[i][total-coins[i]]==-1 :
                dp[i][total-coins[i]]=self.helper(coins,i,total-coins[i],dp)
            ans1=1+dp[i][total-coins[i]]
        if dp[i+1][total]==-1 :
                dp[i+1][total]=self.helper(coins,i+1,total,dp)
            
        ans2=dp[i+1][total]
        
        return min(ans1,ans2)
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for i in range(amount+1)] for i in range(len(coins)+1)]
        ans=self.helperitr(coins,dp)
        # ans=self.helper(coins,0,amount,dp)
        if ans>=sys.maxsize:return -1
        return ans
    