class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr,maxProd = 1,-sys.maxsize
        for i in range(len(nums)):
            if nums[i] ==0:
                curr = 1
                maxProd=max(maxProd,0)
            else:
                curr*=nums[i]
                maxProd=max(maxProd,curr)
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] ==0:
                curr = 1
                maxProd=max(maxProd,0)
            else:
                curr*=nums[i]
                maxProd=max(maxProd,curr) 
        return maxProd

                
