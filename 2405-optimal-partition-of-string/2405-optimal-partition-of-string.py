class Solution:
    def partitionString(self, s: str) -> int:
        d={}
        start=0
        count=1
        for i in range(len(s)):
            letter=s[i]
            if letter in d:
                if d[letter]>=start:
                    count+=1
                    start=i
            d[letter]=i
                    
        return count 
                
                