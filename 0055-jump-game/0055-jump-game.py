class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=0
        r=0
        while r<len(nums)-1:
            fmax=r
            for i in range(l,r+1):
                fmax=max(fmax,i+nums[i])
            if fmax==r:
                return False
            l=r+1
            r=fmax
        return True
                