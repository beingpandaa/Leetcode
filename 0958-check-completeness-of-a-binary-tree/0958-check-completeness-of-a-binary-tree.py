# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        if root:
            q = deque([root])
            nullFound=False
            while q:
                for i in range(len(q)):
                    u=q.popleft()

                    if u.left:
                        if nullFound:return False
                        q.append(u.left)
                    else:
                        nullFound=True 
                    if u.right:
                        if nullFound:return False
                        q.append(u.right)
                    else:
                        nullFound=True 
        return True
                
                
                
                
            