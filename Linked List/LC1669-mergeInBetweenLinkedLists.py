# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        
        cur, i = list1, 0
        while i != b:
            if i + 1 == a:
                tmp = cur.next
                cur.next = list2
                cur = tmp
            else:
                cur = cur.next
            i += 1
        list2_tail.next = cur.next
        return list1