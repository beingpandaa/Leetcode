class Solution:
    def isPalindrome(self,s):
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!=s[j]:return False
            i+=1
            j-=1
        return True
    def getPartitions(self,res,s,sol=[],li=0,i=0):
        if i==len(s):
            if li == len(s):
                res.append(sol[:])
            return
        if self.isPalindrome(s[li:i+1]):
            sol.append(s[li:i+1])
            self.getPartitions(res,s,sol,i+1,i+1)
            sol.pop()
        self.getPartitions(res,s,sol,li,i+1)

    def partition(self, s: str) -> list[list[str]]:
        res = []
        self.getPartitions(res,s)
        return res