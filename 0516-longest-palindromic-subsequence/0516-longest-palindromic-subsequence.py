class Solution:
    def helper(self,s,i,j,d):
        if i>j:return 0
        if i==j:return 1
        if (i,j) in d:return d[(i,j)]
        if s[i]==s[j]:
            d[(i,j)]=2+self.helper(s,i+1,j-1,d)
            return d[(i,j)]
        else:
            ans1=self.helper(s,i+1,j,d)
            ans2=self.helper(s,i,j-1,d)
            d[(i,j)]= max(ans1,ans2)
            return d[(i,j)]
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s,0,len(s)-1,d={})