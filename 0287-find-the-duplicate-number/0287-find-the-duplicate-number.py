class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])]<0:
                oopppssss= abs(nums[i])
                break
            nums[abs(nums[i])]*=-1
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        return oopppssss
            