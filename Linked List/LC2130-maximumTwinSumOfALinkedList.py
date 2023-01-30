# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Add first half to stack and then compare with second half
O(N) time / O(N) space
'''
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        i, stack = 0, []
        cur = head
        while i < n // 2:
            stack.append(cur.val)
            cur = cur.next
            i += 1
        max_twin = 0
        while cur:
            max_twin = max(max_twin, cur.val + stack.pop())
            cur = cur.next
        return max_twin


'''
Reverse second half
O(N) time / O(1) space
'''
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second, max_twin = head, prev, 0
        while first:
            max_twin = max(max_twin, first.val + second.val)
            first = first.next
            second = second.next
        return max_twin