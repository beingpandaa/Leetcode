class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        prev=0
        count=0
        for ele in nums:
            ele+=prev
            prev=ele
            if ele==k:
                count+=1
            if ele-k in d:
                count+=d[ele-k]
            d[ele]=d.get(ele,0)+1
        return count
            
            