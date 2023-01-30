# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        value_counts = defaultdict(int)
        cur = head
        while cur:
            value_counts[cur.val] += 1
            cur = cur.next
        
        dummy = ListNode(0, head)
        prev, cur = dummy, dummy.next
        while cur:
            if value_counts[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next