# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Reverse input lists
O(M + N) time / O(M + N) space
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, l1
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        l1 = prev

        prev, cur = None, l2
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        l2 = prev

        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = carry + l1_val + l2_val
            carry = sum_val // 10
            sum_val %= 10

            cur.next = ListNode(sum_val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        prev, new_head = None, dummy.next
        while new_head:
            tmp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = tmp
        return prev


'''
Stacks
O(M + N) time / O(M + N) space
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            stack2.append(cur.val)
            cur = cur.next
        
        dummy = ListNode()
        cur = dummy
        carry = 0
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            sum_val = carry + val1 + val2
            carry = sum_val // 10
            sum_val %= 10
            cur.next = ListNode(sum_val)
            cur = cur.next
        
        prev, new_head = None, dummy.next
        while new_head:
            tmp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = tmp
        return prev


'''
No extra space
O(M + N) time / O(1) space
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0
        cur = l1
        while cur:
            n1 += 1
            cur = cur.next
        
        cur = l2
        while cur:
            n2 += 1
            cur = cur.next
        
        # Process the longer list if it exists first until the lists are even
        new_list = []
        while n1 > n2:
            new_list.append(l1.val)
            l1 = l1.next
            n1 -= 1
        while n2 > n1:
            new_list.append(l2.val)
            l2 = l2.next
            n2 -= 1

        # Process the remaining elements of the two lists 
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val
            new_list.append(sum_val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Create the new linked list
        dummy = ListNode()
        cur = dummy
        carry, i = 0, len(new_list) - 1
        while i >= 0 or carry:
            val_sum = new_list[i] + carry if i >= 0 else carry
            carry = val_sum // 10
            val_sum %= 10
            cur.next = ListNode(val_sum)
            cur = cur.next
            i -= 1

        # Reverse the new linked list
        new_head, prev = dummy.next, None
        while new_head:
            tmp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = tmp
        return prev
