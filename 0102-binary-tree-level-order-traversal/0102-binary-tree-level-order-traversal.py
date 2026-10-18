# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        op = []
        if not root: return op
        queue = deque([root])
        while queue:
            row = []
            for i in range(len(queue)):
                ele = queue.popleft()
                if ele:
                    row.append(ele.val)
                    if ele.left:queue.append(ele.left)
                    if ele.right:queue.append(ele.right)
            op.append(row)
        return op