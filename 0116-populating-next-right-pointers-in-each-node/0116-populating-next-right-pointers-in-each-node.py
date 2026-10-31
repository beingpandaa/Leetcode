"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        q = deque([])
        if root:q.append(root)
        while q:
            prev = None
            for i in range(len(q)):
                node = q.popleft()
                if prev:
                     prev.next = node
                prev = node
                if node and node.left and node.right: 
                    q.append(node.left)
                    q.append(node.right)
            node.next = None
        return root

