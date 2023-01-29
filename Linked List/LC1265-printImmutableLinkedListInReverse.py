# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.


'''
Double loop
O(N^2) time / O(1) space
'''
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        prev_print = None
        while prev_print != head:
            cur = head
            while cur.getNext() != prev_print:
                cur = cur.getNext()
            prev_print = cur
            cur.printValue()


'''
Recursion
O(N) time / O(N) space
'''
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        def print_list(cur):
            if cur is None:
                return
            
            print_list(cur.getNext())
            cur.printValue()
        print_list(head)


'''
Stack
O(N) time / O(N) space
'''
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        while stack:
            stack.pop().printValue()