# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self,root):
        if not root: return (-1,-1)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return max(2+left[1]+right[1],left[0],right[0]),1+max(right[1],left[1])

    def diameterOfBinaryTree(self, root):        
        return self.dfs(root)[0]


        