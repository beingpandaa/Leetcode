# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
#         p=root.left
#         q=root.right
#         def checkSame(p,q):
#             if not(p or q):return True
#             if not (p and q) or p.val !=q.val :return False
#             return True
        
#         deq=deque([(p,q)])
#         while deq:
#             p,q=deq.popleft()
#             if checkSame(p,q):
#                 if p:
#                     deq.append((p.left,q.right))
#                     deq.append((p.right,q.left))
#             else:
#                 return False
#         return True
        def checkSame(p,q):
            if not(p or q):return True
            if not (p and q) or p.val !=q.val :return False
            return True
        deq=deque([(root.left,root.right)])
        while deq:
            p,q=deq.popleft()
            if checkSame(p,q):
                if p and q:
                    deq.append((p.left,q.right))
                    deq.append((p.right,q.left))
            else:
                return False
        return True