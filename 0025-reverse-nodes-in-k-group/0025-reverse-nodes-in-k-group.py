# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next

        new_head = head
        previous_group_tail = None
        current = head

        for _ in range(length // k):
            group_tail = current
            reversed_head = None
            # Reverse exactly k nodes.
            for _ in range(k):
                next_node = current.next
                current.next = reversed_head
                reversed_head = current
                current = next_node
            # Connect the previous group to this group's new head.
            if previous_group_tail:
                previous_group_tail.next = reversed_head
            else:
                new_head = reversed_head
            # Connect this group's tail to the remaining list.
            group_tail.next = current
            previous_group_tail = group_tail

        return new_head