class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        mi=min(len(word1),len(word2))
        res=''
        while i<mi: 
            res+=word1[i]+word2[i]
            i+=1
        if i!=len(word1):res+=word1[i:]
        if i!=len(word2):res+=word2[i:]
        return res