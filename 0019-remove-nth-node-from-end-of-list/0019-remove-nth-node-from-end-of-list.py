# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        count = 0
        curr = head
        while curr:
            count +=1 
            curr = curr.next
        print(count)
        if not head.next or count == n:return head.next
        curr = head
        for _ in range(count-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
     
