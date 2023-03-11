class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        while r<len(nums)-1:
            flag=r+1
            for i in range(l,r+1):
                flag=max(i+nums[i],flag)
            l=r+1
            r=flag
            count+=1
        return count
            