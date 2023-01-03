# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1_head = l1 = ListNode()
        l2_head = l2 = ListNode()

        cur = head
        while cur:
            if cur.val < x:
                l1.next = cur
                l1 = l1.next
            else:
                l2.next = cur
                l2 = l2.next
            cur = cur.next
        l2.next = None
        l1.next = l2_head.next
        return l1_head.next