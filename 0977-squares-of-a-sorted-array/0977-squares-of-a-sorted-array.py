class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        li=[0]*len(nums)
        for p in range(len(nums)-1,-1,-1):
            if abs(nums[j])>abs(nums[i]):
                li[p]=nums[j]**2
                j-=1
            else:
                li[p]=nums[i]**2
                i+=1
        return li
            
                
            