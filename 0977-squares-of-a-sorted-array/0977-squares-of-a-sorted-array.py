class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r=len(nums)
        li=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                r=i
                break
        l=r-1
                
        while l>-1 and r<len(nums):
            if abs(nums[l])<nums[r]:
                li.append(nums[l]**2)
                l-=1
            else:
                li.append(nums[r]**2)
                r+=1
        while l>-1:
            li.append(nums[l]**2)
            l-=1
        while r<len(nums):
            li.append(nums[r]**2)
            r+=1
        return li
            
                
            