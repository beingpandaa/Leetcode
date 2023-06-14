class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        op = []

        def dfs(r):
            if r is None:
                return
            op.append(r.val)
            dfs(r.left)
            dfs(r.right)
        
        dfs(root)

        op.sort()
        diff = 9999999999
        for i in range(1, len(op)):
            diff = min(diff, op[i] - op[i-1])

        return diff