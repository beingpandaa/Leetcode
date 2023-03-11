# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ans=[]
        while head:
            ans.append(head.val)
            head=head.next
        def makeTree(ans,l,r):
            if l>r:
                return None
            treeNode= TreeNode()
            mid=(r+l)//2
            treeNode.val=ans[mid]
            treeNode.left=makeTree(ans,l,mid-1)
            treeNode.right=makeTree(ans,mid+1,r)
            return treeNode
        return makeTree(ans,0,len(ans)-1)