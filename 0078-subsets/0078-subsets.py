class Solution:
    def findSubsets(self,nums,i=0):
        if i ==len(nums):
            return [[]]
        res = []
        small_op = self.findSubsets(nums,i+1)
        for ele in small_op:
            res.append(ele)
            res.append(ele+[nums[i]])
        return res
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return self.findSubsets(nums)