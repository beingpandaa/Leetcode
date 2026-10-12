class Solution:
    def getCombinations(self,res,candidates,target,i=0,sol=[]):
        if target == 0 :
            res.append(sol[:])
            return
            
        if i == len(candidates):
            return

        if candidates[i] <= target:
            sol.append(candidates[i])
            self.getCombinations(res,candidates,target-candidates[i],i+1,sol)
            sol.pop()
        while i <len(candidates)-1 and candidates[i+1]==candidates[i]: i+=1
        self.getCombinations(res,candidates,target,i+1,sol)

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        self.getCombinations(res,candidates,target)
        return res