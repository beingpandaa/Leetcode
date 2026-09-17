class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        count = 0
        for i in range(len(nums)):
            if i >0:
                nums[i]+=nums[i-1]
            if nums[i]-k in d:
                count +=d[nums[i]-k]
            d[nums[i]] = d.get(nums[i],0)+1
        return count 
