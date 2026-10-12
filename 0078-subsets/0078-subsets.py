class Solution:
    def findSubsets(self,nums,res,i=0,sol = []):
        if i == len(nums):
            res.append(sol[:])
            return
        self.findSubsets(nums,res,i+1,sol)
        sol.append(nums[i])
        self.findSubsets(nums,res,i+1,sol)
        sol.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.findSubsets(nums,res)
        return res