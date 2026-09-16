class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
            maxSum = sys.maxsize * -1
            curr = 0
            for ele in nums:
                curr = curr +ele
                maxSum = max(maxSum,curr)
                curr = max(0,curr)
            return maxSum

