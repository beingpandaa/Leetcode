# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        parent = {}
        ans = []
        q = deque([root])
        # populate the parent map
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left.val] = node
                q.append(node.left)
            if node.right:
                parent[node.right.val] = node
                q.append(node.right)
        visited = set()
        q = deque([target])
        while k>0:

            for i in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    q.append(node.right) 
                if node.val in parent and parent[node.val].val not in visited:
                    q.append(parent[node.val])
            k-=1
         
        while q:
            ans.append(q.popleft().val)
        return ans
                



            



        