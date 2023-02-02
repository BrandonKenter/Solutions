# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, first = dummy, head
        
        while first and first.next:
            second = first.next
            next_first = first.next.next
            
            # Update pointers
            second.next = first
            first.next = next_first
            prev.next = second
            prev = first
            first = next_first
        return dummy.next