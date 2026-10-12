class Solution:
    def findSubsets(self,nums,res,i=0,sol=[]):
        if i == len(nums):
            res.append(sol[:])
            return
        sol.append(nums[i])
        self.findSubsets(nums,res,i+1,sol)
        while i <len(nums)-1 and nums[i+1]==nums[i]:
            i+=1
        sol.pop()
        self.findSubsets(nums,res,i+1,sol)
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.findSubsets(nums,res)
        return res