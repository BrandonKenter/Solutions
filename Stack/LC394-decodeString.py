class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        res = ""
        stack = []
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append(cur_num)
                stack.append(res)
                cur_num = 0
                res = ""
            elif c == ']':
                res = stack.pop() + res * stack.pop()
            else:
                res += c
        return res
            