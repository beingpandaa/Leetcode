# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



                       

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow,count = head,head,0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow : 
                count = 1
                fast = fast.next
                while fast!=slow:
                    count+=1
                    fast=fast.next
                temp = head
                while count:
                    temp = temp.next
                    count-=1
                while temp!=head:
                    temp = temp.next
                    head = head.next
                return head   