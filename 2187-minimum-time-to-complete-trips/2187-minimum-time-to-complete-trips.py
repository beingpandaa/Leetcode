class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def calcTrips(t):
            trips=0
            for ele in time:
                trips+=t//ele
            return trips
        low=1
        high=totalTrips*time[0]
        while low<high:
            mid=(low+high)//2
            trips=calcTrips(mid)
            if trips<totalTrips:
                low=mid+1
            else:
                high=mid
        return low