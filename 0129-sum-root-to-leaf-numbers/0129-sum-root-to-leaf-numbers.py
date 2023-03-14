# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root,total=0):
            if not(root):
                return 0
            total=(total*10) + root.val
            if not(root.left or root.right):return total
            ans1=dfs(root.left,total)
            ans2=dfs(root.right,total)
            return ans1+ans2
        return dfs(root)