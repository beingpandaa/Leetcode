class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        for ele in time:
            r=ele%60
            d[r]=d.get(r,0)+1
        count=0
        for time in d:
            if time==30 or time==0:
                count+= (d[time]*(d[time]-1))//2
            else:
                if 60-time in d:
                    count+=d[time]*d[60-time]
                    d[time]=0
                    d[60-time]=0
        return count
                
            