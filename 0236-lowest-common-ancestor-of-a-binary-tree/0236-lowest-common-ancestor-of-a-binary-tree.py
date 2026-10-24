# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None
    def setLCA(self,root,p,q):

        if not root :
            return False

        left  = self.setLCA(root.left,p,q)
        right = self.setLCA(root.right,p,q)
        if not self.ans:
            curr = root == p or root == q
            if left + right + curr ==2:
                self.ans = root
            return left or right or curr
        return True



    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.setLCA(root,p,q)
        return self.ans




        