class Solution:
    def morris_traversal(self,root):
        current = root
        op=[]
        while current:
            if current.left is None:
                op.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor of current
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right

                # Make current as the right child of its inorder predecessor
                if pre.right is None:
                    pre.right = current
                    current = current.left
                # Revert the changes made to restore the original tree and print current node
                else:
                    pre.right = None
                    op.append(current.val)
                    current = current.right
        return op
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        op = self.morris_traversal(root)
        diff = 9999999999
        for i in range(1, len(op)):
            diff = min(diff, op[i] - op[i-1])

        return diff