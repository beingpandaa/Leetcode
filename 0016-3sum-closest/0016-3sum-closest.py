class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        def pairSum(i):
            tar=target-nums[i-1]
            low=i
            high=len(nums)-1
            res=99999999
            while low<high:
                ele=nums[low]+nums[high]
                if abs(ele-tar)<abs(res-tar):
                    res=ele
                if ele<tar:
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    low+=1
                elif ele>tar:
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    high-=1
                else:
                    return res
            return res
            
            
            
        
        
        
        
        nums.sort()
        i=0
        nearest=9999999
        while i<len(nums)-2:
            res=pairSum(i+1)+nums[i]
            if abs(target-res)<abs(target-nearest):
                nearest=res
                if nearest==target:break
            i+=1
        return nearest
            