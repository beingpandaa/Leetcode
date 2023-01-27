# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSame(p,q):
            if not(p or q):return True
            if not(p and q) or (p.val!=q.val) :return False
            return True
        
        
        r=deque([(p, q)])
        while r:
            p,q=r.popleft()
            if checkSame(p,q):
                if p:
                    r.append((p.left,q.left))
                    r.append((p.right,q.right))
            else:
                return False
        return True
        
            
