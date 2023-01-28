# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        
        def arrPush(root):
            if not root:
                return
            self.arr.append(root.val)
            arrPush(root.left)
            arrPush(root.right)
        arrPush(root)
        return self.arr


            