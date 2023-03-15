# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        num_cc = len(nums)
        while head.next:
            if head.val in nums_set and head.next.val in nums_set:
                num_cc -= 1
            head = head.next
        return num_cc
        