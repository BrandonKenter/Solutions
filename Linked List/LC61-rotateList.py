# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Get the length of the list and the tail node
        last_node, list_length = head, 1
        while last_node.next:
            list_length += 1
            last_node = last_node.next
        
        # Find how many shifts we need to do
        k = (list_length + k) % list_length
        if k == 0: return head

        # Iterate to the new tail node using k
        idx = 1
        cur = head
        while idx != list_length - k:
            idx += 1
            cur = cur.next
        
        # Update pointers
        new_head = cur.next
        cur.next = None
        last_node.next = head
        return new_head