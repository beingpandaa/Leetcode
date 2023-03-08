# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans=0
        if root:
            deq=deque([root])
            while deq:
                for i in range (len(deq)):
                    ele=deq.popleft()
                    if ele.right:deq.append(ele.right)
                    if ele.left:deq.append(ele.left)
                ans+=1
        return ans
                
                
            