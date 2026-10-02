# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#         p-c
#           h
# n-n-n-n-n-n

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head 
        prev = None
        while head:
            head = head.next
            curr.next = prev
            prev = curr
            curr = head 
        return prev
        
