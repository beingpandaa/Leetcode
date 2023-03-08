class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        def calcHours(rate):
            hr=0
            for pile in piles:
                hr+=(pile//rate)+(pile%rate!=0)
            return hr
                
        while low<high:
            mid=(high+low)//2
            time=calcHours(mid)
            if time>h:
                low=mid+1
            else:
                high=mid
        return low
            