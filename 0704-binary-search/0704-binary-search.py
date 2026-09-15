class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        while left<=right:
            mid = left+((right-left)//2) 
            # mid = (l+r)//2   donot use this as this can cause integer overflow(safe in python)
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return mid
        return -1