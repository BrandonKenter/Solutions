class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        
        for p in s:
            if p in close_to_open:
                if stack and stack[-1] == close_to_open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False