class Solution:
    def ap(self,num):
        return ((num+1)*num//2)
    def total(self,index,n,tar):
        lsum=self.ap(tar-1)
        
        rsum=lsum
        lLeftover=n-1-index
        rLeftover=index
        
        if lLeftover<=tar-1:
            lsum-=self.ap(tar-1-lLeftover)
            
        elif lLeftover>tar-1:
            lsum+=(lLeftover-(tar-1))
            
        if rLeftover <=tar-1:
            rsum-=self.ap(tar-1-rLeftover)
        elif rLeftover>tar-1:
            rsum+=(rLeftover-(tar-1))   
        return lsum+rsum+tar
            
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # target will range from lowest 1 to highest maxSum
        low=1
        high=maxSum
        while low<high:
            mid=(low+high+1)//2
            if self.total(index,n,mid)>maxSum:
                high=mid-1
            else:
                low=mid
        return low
    