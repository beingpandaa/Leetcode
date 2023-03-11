class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        leftOverCards=n-k
        if leftOverCards==0:
            return sum(cardPoints)
        l=0
        r=l+leftOverCards-1
        for i in range(1,len(cardPoints)):
            cardPoints[i]+=cardPoints[i-1]
        
        ans=0
        while r<len(cardPoints):
            if l==0:
                ans=max(ans,cardPoints[n-1]-cardPoints[r])
            else:
                ans=max(ans,cardPoints[n-1]-(cardPoints[r]-cardPoints[l-1]))
            l+=1
            r+=1
        return ans
            
            