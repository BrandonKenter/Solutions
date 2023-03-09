class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {'U' : [-1, 0], 'D' : [1, 0], 'R' : [0, 1], 'L' : [0, -1]}
        
        res = []
        for i in range(len(s)):
            dist = 0
            r, c = startPos
            for j in range(i, len(s)):
                d = s[j]
                nei_r, nei_c = r + directions[d][0], c + directions[d][1]
                if (
                    nei_r in range(n) and 
                    nei_c in range(n)
                ):
                    dist += 1
                    r = nei_r
                    c = nei_c
                else:
                    break
            res.append(dist)
        return res
        