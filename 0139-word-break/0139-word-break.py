class Solution:
    def helper(self,s,i,st,d={}):
        if i==len(s):return 1

        for j in range(i+1,len(s)+1):
            if s[i:j] in st:
                if j not in d:d[j]=self.helper(s,j,st,d)
                if d[j]==1:return 1
        return 0
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st=set(wordDict)
        return self.helper(s,0,st,{})