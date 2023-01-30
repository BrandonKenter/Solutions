# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The first node is guaranteed to be 0
        # The second node is guaranteed to be non-zero
        prev, cur = head.next, head.next.next
        while cur:
            # If current is 0, update the reference of the first node in this
            # section between two zeroes to the first node in the next section
            # 0 -> 3 -> 1 -> __0__ -> 4 -> 5 -> 2 -> 0 : at this 0 this case executes
            if cur.val == 0:
                prev.next = cur.next
                prev = prev.next
                # If on last 0, we are done merging. Otherwise, continue
                # 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> __0__ : at this 0 this case executes
                if not cur.next: break
                # 0 -> 3 -> 1 -> __0__ -> 4 -> 5 -> 2 -> 0 : at this 0 this case executes
                else: cur = cur.next.next

            # Otherwise current is not 0, increment the first node in this segment's
            # value by the current node's value
            # 0 -> 3 -> __1__ -> 0 -> 4 -> 5 -> 2 -> 0 : at this non-zero value this case executes
            else:
                prev.val += cur.val
                cur = cur.next
        # To discard the first 0, just return head.next
        # The list is guaranteed to have trhee nodes, where the first and last are 0's
        return head.next