# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        lenA, lenB = 1, 1
        while A:
            A = A.next
            lenA += 1
        while B:
            B = B.next
            lenB += 1
        
        if lenA > lenB:
            while lenA != lenB:
                headA = headA.next
                lenA -= 1
        if lenB > lenA:
            while lenA != lenB:
                headB = headB.next
                lenB -= 1
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None