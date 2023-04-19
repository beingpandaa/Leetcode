# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        
        if not root:return (-1,-1,0)
        ans1=self.helper(root.left)
        ans2=self.helper(root.right)
        lef_bak,lef_for=ans1[0],ans1[1]
        rig_bak,rig_for=ans2[0],ans2[1]
        overall_max=max(ans1[2],ans2[2])
        including_max=1+max(lef_for,rig_bak)
        return lef_for+1,rig_bak+1,max(overall_max,including_max)
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:  return self.helper(root)[2]
        