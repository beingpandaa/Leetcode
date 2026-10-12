class Solution:
    def findSubsets(self,nums,i,sol,res):
        if i == len(nums):
            res.append(sol[:])
            return
        self.findSubsets(nums,i+1,sol,res)
        sol.append(nums[i])
        self.findSubsets(nums,i+1,sol,res)
        sol.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.findSubsets(nums,0,[],res)
        return res