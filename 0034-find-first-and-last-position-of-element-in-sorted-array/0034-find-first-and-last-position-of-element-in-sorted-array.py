class Solution(object):
    def lowerBound(self,nums,target):
        left = 0
        right = len(nums)-1
        ans = right + 1
        while left <= right :
            mid = left+(right-left)//2
            if nums[mid] >= target:
                right = mid-1
                ans = mid
            else:
                 left = mid + 1
        return ans
    def upperBound(self,nums,target):
        left = 0
        right = len(nums)-1
        ans = right + 1
        while left <= right :
            mid = left+(right-left)//2
            if nums[mid] > target:
                right = mid-1
                ans = mid
            else:
                 left = mid + 1
        return ans
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lb = self.lowerBound(nums,target)
        if lb == len(nums) or nums[lb]!=target:return [-1,-1]
        return [lb,self.upperBound(nums,target)-1]
        