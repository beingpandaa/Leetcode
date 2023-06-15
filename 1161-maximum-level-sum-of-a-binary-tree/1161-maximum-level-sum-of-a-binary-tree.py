# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lv=1
        res=root.val
        q=deque([root])
        currLevel=1
        while q:
            curr=0
            for i in range(len(q)):
                ele=q.popleft()
                curr+=ele.val
                if ele.left:q.append(ele.left)
                if ele.right:q.append(ele.right)
            if curr>res:
                res=curr
                lv=currLevel
            currLevel+=1
        return lv
                
            
        
            
        