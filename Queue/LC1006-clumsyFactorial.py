class Solution:
    def clumsy(self, n: int) -> int:
        q = deque([str(n)])
        j = 0
        for i in range(n-1, 0, -1):
            if j % 4 == 0:
                q.append(str(int(q.pop()) * i))
            elif j % 4 == 1:
                q.append(str(int(q.pop()) // i))
            elif j % 4 == 2:
                q.append('+')
                q.append(str(i))
            else:
                q.append('-')
                q.append(str(i))
            j += 1
        
        while len(q) > 1:
            l_operand = q.popleft()
            operator = q.popleft()
            r_operand = q.popleft()
            if operator == '+':
                q.appendleft(str(int(l_operand) + int(r_operand)))
            else:
                q.appendleft(str(int(l_operand) - int(r_operand)))
        return int(q[0])
