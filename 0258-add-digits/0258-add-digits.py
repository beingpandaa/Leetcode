class Solution:
    def addDigits(self, n: int) -> int:
        curr=0
        while n>9:
            curr=0
            while n>0:
                curr+=n%10
                n=n//10
            n=curr
        return n
            
            