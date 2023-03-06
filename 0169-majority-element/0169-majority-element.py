class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        maxf=0
        max_ele=nums[0]
        for ele in nums:
            d[ele]=d.get(ele,0)+1
            if d[ele]>maxf:
                maxf=d[ele]
                max_ele=ele
        return max_ele
                
            
            