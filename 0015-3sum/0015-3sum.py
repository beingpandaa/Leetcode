class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        li=[]
        def twoSome(low,tar):
            high=len(nums)-1
            while low<high:
                if nums[low]+nums[high]<tar:
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    low+=1
                elif  nums[low]+nums[high]>tar:
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    high-=1
                else:
                    li.append([-tar,nums[low],nums[high]])
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    high-=1
        i=0
        while i<len(nums)-2:
            twoSome(i+1,-nums[i])
            while i+1<len(nums)-2 and nums[i+1]==nums[i]:
                i+=1
            i+=1
        return li
        
                    
            
                
                    
                    
                
            
        