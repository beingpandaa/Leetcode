# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, headA: ListNode | None, headB: ListNode | None) -> ListNode | None:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while headA or headB or carry:
            n =  carry
            if headA:
                n+=headA.val
                headA = headA.next
            if headB:
                n+=headB.val
                headB = headB.next
            carry = n//10
            curr.next = ListNode(n%10)
            curr = curr.next
        
        return dummy.next

            
