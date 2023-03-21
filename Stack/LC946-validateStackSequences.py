'''
Explicit stack
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = j = 0
        while i < len(pushed) and j < len(popped):
            if not stack or stack[-1] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                stack.pop()
                j += 1
        if i < len(pushed):
            return True
        while j < len(popped):
            if not stack or stack[-1] != popped[j]:
                return False
            stack.pop()
            j += 1
        return True
        