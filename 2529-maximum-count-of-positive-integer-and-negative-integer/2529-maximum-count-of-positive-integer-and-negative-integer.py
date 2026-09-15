class Solution:
    def findJustGreater(self,nums,left,right,target):
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid-1
        return left
    def maximumCount(self, nums: List[int]) -> int:
        if (nums[0]>0 and nums[-1]>0) or (nums[0]<0 and nums[-1]<0):return len(nums) 
        neg = self.findJustGreater(nums,0,len(nums)-1,-1)
        pos = self.findJustGreater(nums,neg,len(nums)-1,0)
        print(neg,pos)
        return max(neg,len(nums)-pos)
        
        
        