class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {nums[0]%k:1}
        for i in range(1,len(nums)):
            rem = nums[i] % k
            nums[i] = nums[i]+nums[i-1]
            prefixRem = nums[i]%k
            if prefixRem == 0 : return True
            if rem == 0 : 
                if d.get(prefixRem,0)>1: return True
            else:
                if prefixRem in d: return True
            d[prefixRem] = d.get(prefixRem,0)+1
        return False

