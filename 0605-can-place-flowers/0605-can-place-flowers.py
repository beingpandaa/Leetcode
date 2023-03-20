class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==0:
                
                left=(i==0) or (flowerbed[i-1]==0)
                right=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if left and right:
                    flowerbed[i]=1
                    count+=1
            i+=1
     
        return count>=n

            