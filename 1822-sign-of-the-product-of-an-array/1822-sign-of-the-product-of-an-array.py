class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=0
        for ele in nums:
            if ele==0:
                return 0
            if ele<0:neg+=1
        if neg^1==neg+1:return 1
        return -1