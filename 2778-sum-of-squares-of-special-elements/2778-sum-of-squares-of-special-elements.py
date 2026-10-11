from math import isqrt
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        mid_index = isqrt(len(nums))
        for i in range(mid_index):
            index = i+1
            if len(nums)%(index)==0:
                res+=nums[i]*nums[i]
                temp = len(nums)//index
                if index!=temp:
                    res+=nums[temp-1]*nums[temp-1]
        return res

