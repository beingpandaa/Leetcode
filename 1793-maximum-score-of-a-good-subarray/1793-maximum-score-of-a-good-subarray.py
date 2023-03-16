class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack=[]
        ps=[]
        ns=[0]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                ps.append(stack[-1])
            else:
                ps.append(-1)
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:stack.pop()
            if stack:ns[i]=stack[-1]
            else:ns[i]=len(nums)
            stack.append(i)
        maxScore=0
        for i in range(len(nums)):
            low,high=ps[i],ns[i]
            if low+1<=k<=high-1:
                maxScore=max(maxScore,(high-low-1)*nums[i])
        return maxScore