class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kv = {}
        for key, value in knowledge:
            kv[key] = value
        
        res = []
        i = j = 0
        while i < len(s):
            if s[i] == '(':
                while s[j] != ')':
                    j += 1
                k = s[i+1:j]
                res.append(kv[k] if k in kv else '?')
                i = j + 1
                j = i
            else:
                res.append(s[i])
                i += 1
        return "".join(res)
        