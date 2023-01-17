class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        def part_on_top():
            j = n - 1
            for i in range(1, n + 1):
                if stack[-i] != part[j]:
                    return False
                j -= 1
            return True

        n = len(part)
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= n and part_on_top():
                for i in range(n):
                    stack.pop()   
        return "".join(stack)