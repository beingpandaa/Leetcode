# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None : return head 
        even,odd = ListNode(0),ListNode(0)
        evenptr,oddptr =even,odd
        isOdd = True
        while head:
            if isOdd:
                oddptr.next = head
                oddptr = head
            else:
                evenptr.next = head
                evenptr = head
            head = head.next
            isOdd = 0 if isOdd else 1
        evenptr.next =None
        oddptr.next = even.next
        return odd.next