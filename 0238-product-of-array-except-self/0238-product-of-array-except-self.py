class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:li[i]=nums[i]
            else:li[i]=nums[i]*li[i+1]
        for i in range(1,len(nums)):
            nums[i]*=nums[i-1]
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:res[i]=li[i+1]
            elif i==len(nums)-1:res[i]=nums[i-1]
            else:res[i]=li[i+1]*nums[i-1]
        return res