# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=deque([root])
        op=[]
        res=0
        lv=0
        while q:
            curr=0
            for i in range(len(q)):
                ele=q.popleft()
                curr+=ele.val
                if ele.left:q.append(ele.left)
                if ele.right:q.append(ele.right)
            lv+=1
            op.append(curr)
        
        op.sort()
        print(op)
        
        return -1 if lv<k else op[-k]
            
            