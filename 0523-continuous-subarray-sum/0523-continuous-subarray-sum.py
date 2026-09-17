class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {0:-1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            rem = currSum % k
            if rem not in d:
                d[rem] = i
            elif i-d[rem]>1: return True
        return False


