class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twoSome(low,x,y):
            tar=target-x-y
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
                    li.append([x,y,nums[low],nums[high]])
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    high-=1
                    
        nums.sort()
        li=[]
        i=0
        while i < len(nums)-3:
            j=i+1
            while j<len(nums)-2:
                twoSome(j+1,nums[i],nums[j])
                while j+1<len(nums)-2 and nums[j+1]==nums[j]:
                    j+=1
                j+=1
            while i+1<len(nums)-2 and nums[i+1]==nums[i]:
                i+=1
            i+=1
        return li