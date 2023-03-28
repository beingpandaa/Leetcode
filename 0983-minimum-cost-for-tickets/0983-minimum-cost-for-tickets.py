class Solution:
    
    def helper(self,days,costs,i,deepee):
        if i==len(days):
            return 0
        
        if deepee[i+1]==-1:deepee[i+1]=self.helper(days,costs,i+1,deepee)
        ans1=costs[0]+deepee[i+1]
        curr=i
        for index in range(curr,len(days)):
            if days[index]<days[i]+7:
                curr+=1
            else:
                break
        if deepee[curr]==-1:deepee[curr]=self.helper(days,costs,curr,deepee)
        ans2=costs[1]+deepee[curr]
        curr=i
        for index in range(curr,len(days)):
            if days[index]<days[i]+30:
                curr+=1
            else:
                break
        if deepee[curr]==-1:deepee[curr]=self.helper(days,costs,curr,deepee)
        ans3=costs[2]+deepee[curr]
        
        return min(ans1,ans2,ans3)
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        deepee=[-1 for i in range(len(days)+1)]
        return self.helper(days,costs,0,deepee)