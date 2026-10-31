class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while a and b:
            if a == b: return a
            a=a.next
            b=b.next
            if not a:a = headB
            elif not b:b = headA

