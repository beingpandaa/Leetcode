class Solution:

    def getCombinations(self,res,candidates,target,i=0,sol=[]):
        if target == 0 :
            res.append(sol[:])
            return
            
        if i == len(candidates):
            return

        if candidates[i] <= target:
            sol.append(candidates[i])
            self.getCombinations(res,candidates,target-candidates[i],i,sol)
            sol.pop()
        self.getCombinations(res,candidates,target,i+1,sol)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        self.getCombinations(res,candidates,target)
        return res