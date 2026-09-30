class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        curr = 0
        res = []
        for bracket in seq:
            if bracket == "(":
                curr+=1
                res.append(curr%2)
            else:
                res.append(curr%2)
                curr-=1    
        return res