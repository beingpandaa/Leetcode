class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currL,currR,maxProd = 1,1,-sys.maxsize
        for i in range(len(nums)):
            len(nums)-i-1
            if nums[i] ==0:
                currL = 1
                maxProd=max(maxProd,0)
            else:
                currL*=nums[i]
                maxProd=max(maxProd,currL)

            if nums[len(nums)-i-1] ==0:
                currR = 1
                maxProd=max(maxProd,0)
            else:
                currR*=nums[len(nums)-i-1]
                maxProd=max(maxProd,currR)

        return maxProd

                
