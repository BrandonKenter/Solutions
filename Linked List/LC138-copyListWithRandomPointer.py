"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None : None}
        old = head
        while old:
            new = Node(old.val)
            old_to_new[old] = new
            old = old.next
        
        old = head
        while old:
            new = old_to_new[old]
            new.next = old_to_new[old.next]
            new.random = old_to_new[old.random]
            old = old.next
        return old_to_new[head]