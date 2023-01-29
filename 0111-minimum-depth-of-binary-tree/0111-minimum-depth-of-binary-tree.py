# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        ans=0
        if root:
            deq=deque([root])
            level=deque([])
            while deq:
                for i in range(len(deq)):
                    ele=deq.popleft()
                    if not(ele.left or ele.right):
                        ans+=1
                        return ans
                    else:
                        if ele.right:level.append(ele.right)
                        if ele.left:level.append(ele.left)
                ans+=1
                deq=level
        return ans
            
            
                
                    
        