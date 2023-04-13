class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        i=0
        j=len(nums)-1
        prodi=1
        prodj=1
        overall=nums[i]
        while i<len(nums):
            if nums[i]==0:
                overall=max(overall,0)
                prodi=1
                
            else:
                prodi*=nums[i]
                overall=max(overall,prodi)
            if nums[j]==0:
                overall=max(overall,0)
                prodj=1
            else:
                prodj*=nums[j]
                overall=max(overall,prodj)
            i+=1
            j-=1
        return overall
            
#         mi=1
#         ma=1
#         overallMax=max(nums)
        
#         for ele in nums:
            
#             if ele==0:
#                 mi=1
#                 ma=1
                
#             elif ele>0:
               
#                 ma=ma*ele
#                 mi=min(1,mi*ele)
#                 overallMax=max(overallMax,ma)
#             else:
#                 temp=mi
#                 mi=ma*ele
#                 ma=max(1,temp*ele)
            
#                 overallMax=max(overallMax,ma)
         
#         return overallMax
    