'''
Manually reverse, filter, reverse
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, count = None, 0
        while head:
            count += 1
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        valid = [0 for i in range(count)]
        head, i = prev, count - 1
        maxi = head.val
        valid[-1] = 1
        cur = head
        while cur:
            if cur.val >= maxi:
                maxi = cur.val
                valid[i] = 1
            i -= 1
            cur = cur.next
        
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        head = prev

        dummy = ListNode(0, head)
        left = dummy
        cur = dummy.next
        i = 0
        while cur:
            if valid[i]:
                left.next = cur
                left = cur
            cur = cur.next
            i += 1
        return dummy.next


'''
Monotonically decreasing stack
Preferable solution
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        
        dummy = ListNode()
        cur = dummy
        for node in stack:
            cur.next = node
            cur = cur.next
        return dummy.next
