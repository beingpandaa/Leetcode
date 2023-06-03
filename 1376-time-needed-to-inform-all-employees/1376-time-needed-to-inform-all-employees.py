class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d={}
        for i in range(n):
            if manager[i] in d:
                d[manager[i]].append(i)
            else:
                d[manager[i]]=[i]
        deq=deque([(headID,0)])
        res=0
        while deq:
            i,time=deq.popleft()
            res=max(res,time)
            if i in d:
                for emp in d[i]:
                    deq.append((emp,time+informTime[i]))
        return res   
                