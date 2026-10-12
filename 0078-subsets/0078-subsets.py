class Solution:
    def findSubsets(self,nums,res,i=0,sol = []):
        if i == len(nums):
            res.append(sol[:])
            return        
        sol.append(nums[i])
        self.findSubsets(nums,res,i+1,sol)
        sol.pop()
        self.findSubsets(nums,res,i+1,sol)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.findSubsets(nums,res)
        return res