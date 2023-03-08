# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getMaxDepth(root):
    
            if not root:return 0
        
            ans1=getMaxDepth(root.left)
            ans2=getMaxDepth(root.right)
            return max(ans1,ans2)+1
        
        return getMaxDepth(root)
                
            