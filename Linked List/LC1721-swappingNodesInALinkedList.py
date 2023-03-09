# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next: return head
        
        beg = head
        end = head
        end_r = head
        i = 1
        while i != k:
            beg = beg.next
            end_r = end_r.next
            i += 1

        while end_r.next:
            end = end.next
            end_r = end_r.next
        
        beg.val, end.val = end.val, beg.val
        return head
