# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, headA: ListNode | None, headB: ListNode | None) -> ListNode | None:
        dummy = temp = ListNode(0)
        while headA and headB:
            if headA.val<headB.val:
                temp.next = headA
                headA = headA.next
            else:
                temp.next = headB
                headB = headB.next
            temp = temp.next
        temp.next = headA or headB
        return dummy.next
        
