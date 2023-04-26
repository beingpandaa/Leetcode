class Solution:
    def addDigits(self, n: int) -> int:
        if n == 0:return 0
        if n % 9 == 0:return 9
        return n % 9
        # curr=0
        # while n>9:
        #     curr=0
        #     while n>0:
        #         curr+=n%10
        #         n=n//10
        #     n=curr
        # return n
            
            