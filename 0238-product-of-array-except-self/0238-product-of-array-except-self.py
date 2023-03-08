class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:li[i]=nums[i]
            else:li[i]=nums[i]*li[i+1]
        prev=1
        for i in range(len(nums)):
            if i==0:li[i]=li[i+1]
            elif i==len(nums)-1:li[i]=nums[i-1]
            else:li[i]=li[i+1]*nums[i-1]
            nums[i]=nums[i]*prev
            prev=nums[i]
        return li