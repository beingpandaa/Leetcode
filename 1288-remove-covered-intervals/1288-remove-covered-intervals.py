class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        print(intervals)
        res,curr = 0,0
        for ele in intervals:
            if ele[1]>curr:res+=1
            curr = max(curr,ele[1])
        return res