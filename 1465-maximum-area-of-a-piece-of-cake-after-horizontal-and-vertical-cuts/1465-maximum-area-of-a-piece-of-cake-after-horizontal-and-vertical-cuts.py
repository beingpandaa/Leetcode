class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        fmax=horizontalCuts[0]
        for i in range(1,len(horizontalCuts)):
            fmax=max(fmax,horizontalCuts[i]-horizontalCuts[i-1])
        
        vmax=verticalCuts[0]
        for i in range(1,len(verticalCuts)):
            vmax=max(vmax,verticalCuts[i]-verticalCuts[i-1])
            
       
        return fmax*vmax%(1000000007)
        