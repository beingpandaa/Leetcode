class Solution:
    def helper(self,piles,i,k,d):
        if k==0 or i==len(piles):return 0
        if (i+1,k) not in d:d[(i+1,k)]=self.helper(piles,i+1,k,d)
        ans=d[(i+1,k)]
        for ind in range(min(k,len(piles[i]))):
            if (i+1,k-ind-1) not in d:d[(i+1,k-ind-1)]=self.helper(piles,i+1,k-ind-1,d)
            ans=max(ans,piles[i][ind]+d[(i+1,k-ind-1)])
        return ans
            
            
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i in range(len(piles)):
            curr=0
            for j in range(len(piles[i])):
                piles[i][j]+=curr
                curr=piles[i][j]
        
        return self.helper(piles,0,k,d={})