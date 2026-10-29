class Solution:
    def calcHours(self,rate,piles):
        hr=0
        for pile in piles:
            hr+=(pile//rate)+(pile%rate!=0)
        return hr
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low,high= 1,max(piles)
        ans = high
        while low<=high:
            mid =  low+(high-low)//2
            time = self.calcHours(mid,piles)
            if time>h:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans