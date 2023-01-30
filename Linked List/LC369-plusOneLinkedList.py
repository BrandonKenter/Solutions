# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Single pass
O(N) time / O(1) space
'''
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        not_nine, cur = dummy, head

        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next

        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        return dummy if dummy.val else dummy.next


'''
Triple pass
O(N) time / O(N) space
'''
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        new_list = ListNode()
        new_cur = new_list
        head = prev
        cur, carry = head, 1
        while cur or carry:
            digit = cur.val + carry if cur else carry
            carry = digit // 10
            digit %= 10
            new_cur.next = ListNode(digit)
            cur = cur.next if cur else None
            new_cur = new_cur.next
        
        head, prev = new_list.next, None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev