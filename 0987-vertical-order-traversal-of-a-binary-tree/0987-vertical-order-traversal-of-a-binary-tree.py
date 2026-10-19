# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        if not root: return []
        d={}
        q = deque([(root,0)])  #[(node,level,position(2k-1 || 2k))] 
        level = 0       
        while q:
            for i in range(len(q)):
                node,pos = q.popleft()
                if pos not in d: d[pos]=[]
                d[pos].append((node.val,level))
                if node.left:q.append((node.left,pos-1))
                if node.right:q.append((node.right,pos+1))
            level+=1
        keys = d.keys()
        keys.sort()
        op = []
        for key in keys:
            row = d[key]
            row.sort(key=lambda x: (x[1], x[0]))
            op.append([ele[0] for ele in row])
        return op

            

        