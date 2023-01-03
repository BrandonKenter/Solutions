'''
Iterative
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

'''
Recursive
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(cur, prev):
            if cur is None:
                return prev
            
            tmp = cur.next
            cur.next = prev
            return helper(tmp, cur)
        return helper(head, None)