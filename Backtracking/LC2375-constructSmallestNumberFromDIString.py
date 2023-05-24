class Solution:
    def smallestNumber(self, pattern: str) -> str:
        s = []
        used = set()

        def backtrack(i):
            if i == len(pattern) + 1:
                return "".join(s)
            
            for j in range(1, 10):
                if len(s) == 0:
                    s.append(str(j))
                    used.add(j)
                    take = backtrack(i+1)
                    if take:
                        return take
                    s.pop()
                    used.remove(j)
                else:
                    if pattern[i-1] == 'I':
                        if j <= int(s[-1]) or j in used:
                            continue
                        s.append(str(j))
                        used.add(j)
                        take = backtrack(i+1)
                        if take:
                            return take
                        s.pop()
                        used.remove(j)
                    else:
                        if j >= int(s[-1]) or j in used:
                            continue
                        s.append(str(j))
                        used.add(j)
                        take = backtrack(i+1)
                        if take:
                            return take
                        s.pop()
                        used.remove(j)
            return None

        return backtrack(0)
                                  