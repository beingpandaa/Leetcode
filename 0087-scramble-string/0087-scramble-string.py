class Solution:
    def helper(self,s,t,d):
        if s==t:return True
        for i in range(len(s)-1):
            # if not swap
            if (s[:i+1],t[:i+1]) not in d:d[(s[:i+1],t[:i+1])]=self.helper(s[:i+1],t[:i+1],d)
            if (s[i+1:],t[i+1:]) not in d:d[(s[i+1:],t[i+1:])]=self.helper(s[i+1:],t[i+1:],d)    
            ans1=d[(s[:i+1],t[:i+1])]
            ans2=d[(s[i+1:],t[i+1:])]
            if ans1 and ans2:return True
            
            # if swap
            if (s[:i+1],t[-i-1:]) not in d:d[(s[:i+1],t[-i-1:])]=self.helper(s[:i+1],t[-i-1:],d)
            if (s[i+1:],t[:-i-1]) not in d:d[(s[i+1:],t[:-i-1])]=self.helper(s[i+1:],t[:-i-1],d) 
            ans1=d[(s[:i+1],t[-i-1:])]
            ans2=d[(s[i+1:],t[:-i-1])]
            if ans1 and ans2:return True
        return False
        
    def isScramble(self, s: str, t: str) -> bool:
            d={}
            return self.helper(s,t,d)
        