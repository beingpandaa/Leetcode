class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a and b:
            a=a.next
            b=b.next
        count = 0 
        small = None
        big = None
        temp = None
        if a:
            small = headB
            big = headA 
            temp = a          
        else:
            small = headA
            big = headB
            temp = b
        while temp:
            count+=1
            temp = temp.next
        while count:
            count-=1
            big=big.next
        
        while big!=small:
            big = big.next
            small = small.next

        return small

