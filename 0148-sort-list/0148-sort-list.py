# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmid(self,head):
        if head and head.next:
            fast,slow = head.next,head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        return head
    
    def merge(self,head1,head2):
        dummy = ListNode()
        temp = dummy
        while head1 and head2:
            if head1.val <head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        head = head1 or head2
        while head:
            temp.next = head
            head = head.next
            temp = temp.next
        return dummy.next
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        mid = self.findmid(head)
        head2 = mid.next
        mid.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        return self.merge(head1,head2)
        
