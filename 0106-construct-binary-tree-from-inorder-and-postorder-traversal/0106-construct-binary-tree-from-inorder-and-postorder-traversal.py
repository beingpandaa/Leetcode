# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, ino: List[int], post: List[int]) -> Optional[TreeNode]:
        
        
        d={}
        for i in range(len(ino)):
            d[ino[i]]=i
            
            

            
        def dfs(ins,ie,ps,pe):
            if ps>pe or ins>ie:
             
                return None
            
            root=TreeNode(post[pe])
            index=d[root.val]
            
            root.left=dfs(ins,index-1,ps,ps+(index-ins)-1)
          
            root.right=dfs(index+1,ie,ps+(index-ins),pe-1)
            return root
        return dfs(0,len(ino)-1,0,len(post)-1)
            
            