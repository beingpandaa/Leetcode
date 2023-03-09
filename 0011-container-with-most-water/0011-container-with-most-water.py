class Solution:
    def maxArea(self, nums: List[int]) -> int:
        high=len(nums)-1
        low=0
        ans=0
        while low<high:
            if nums[low]<nums[high]:
                ans=max(ans,(high-low)*nums[low])
                low+=1
            elif nums[high]<nums[low]:
                ans=max(ans,(high-low)*nums[high])
                high-=1
            else:
                ans=max(ans,(high-low)*nums[high])
                high-=1
                low+=1
        return ans