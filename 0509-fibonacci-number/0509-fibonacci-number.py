class Solution:
    def fib(self, n: int) -> int:
        if n<2:return n
        a=0
        b=1
        c=1
        while c<n:
            b=a+b
            a=b-a
            c+=1
        return b
        