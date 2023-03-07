class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergerList=[]
        for interval in intervals:
            if len(mergerList)==0 or mergerList[-1][1]<interval[0]: mergerList.append(interval)
            else: mergerList[-1][1]=max(mergerList[-1][1],interval[1])
        return mergerList
                