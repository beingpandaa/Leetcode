class Solution:
    def findIndex(self,potions,mul,j,tar):
        i=0
        index=len(potions)
        while i<=j:
            mid=(i+j)//2
            if potions[mid]*mul>=tar:
                index=mid
                j=mid-1
            else:
                i=mid+1
        return index
                
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        
        arr=sorted(spells)
        potions.sort()
        d={}
        j=len(potions)-1
        for ele in arr:
            if ele not in d:
                index=self.findIndex(potions,ele,j,success)
                # print(index)
                d[ele]=len(potions)-index
                if index!=len(potions):
                    j=index
        li=[]
        for ele in spells:
            li.append(d[ele])
        return li
            