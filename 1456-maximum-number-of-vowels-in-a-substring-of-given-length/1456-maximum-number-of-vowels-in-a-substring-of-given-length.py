class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t={'a','e','i','o','u'}
        count=0
        for i in range(k):
            if s[i] in t:count+=1
        i=0
        j=k-1
        max_count=count
        while j<len(s)-1:
            if s[i] in t:count-=1
            if s[j+1] in t:count+=1
            i+=1
            j+=1
            max_count=max(max_count,count)
        return max_count
            