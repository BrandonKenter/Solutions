# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            i = 1
            while cur and i != m:
                cur = cur.next
                i += 1
                
            if not cur: return head

            right = cur
            j = 0
            while right and j != n + 1:
                right = right.next
                j += 1
            
            cur.next = right
            cur = cur.next
        return head