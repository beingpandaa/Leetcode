class Solution:
    def reverseDegree(self, s: str) -> int:
        prodSum = 0
        for i in range (len(s)):prodSum+=((i+1)*(123-ord(s[i])))
        return prodSum