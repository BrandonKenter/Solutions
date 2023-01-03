class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                r_num, l_num = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l_num + r_num)
                elif t == '-':
                    stack.append(l_num - r_num)
                elif t == '*':
                    stack.append(l_num * r_num)
                else:
                    stack.append(int(float(l_num) / r_num))
        return stack[-1]