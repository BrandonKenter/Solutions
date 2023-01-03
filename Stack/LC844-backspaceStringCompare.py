class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        q1 = deque()
        q2 = deque()
        
        for c in s:
            if c == '#':
                if q1:
                    q1.pop()
            else:
                q1.append(c)
        
        for c in t:
            if c == '#':
                if q2:
                    q2.pop()
            else:
                q2.append(c)
        return q1 == q2