class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in d:return [i,d[rem]]
            d[nums[i]]=i

            