class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        for ele in s:
            if ele == "(":
                curr_depth+=1
            elif ele == ")":
                curr_depth-=1
            max_depth = max(max_depth,curr_depth)
        return max_depth