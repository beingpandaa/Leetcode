class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        de=collections.deque(list(senate))
        r_count = senate.count('R')
        d_count = len(senate) - r_count
        r=0
        d=0
        while de:
            for i in range(len(de)):
                ele=de.popleft()
                if ele=='R':
                    if d>0:
                        d-=1
                        r_count-=1
                    else:
                        r+=1
                        de.append(ele)
                else:
                    if r>0:
                        r-=1
                        d_count-=1
                    else:
                        d+=1
                        de.append(ele)
            
            if d_count==0:return "Radiant"
            elif r_count==0: return "Dire"
                    
            