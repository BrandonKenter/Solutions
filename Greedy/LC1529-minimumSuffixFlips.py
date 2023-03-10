class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        if target[0] == '1':
            flips = 1
        
        cur = target[0]
        for i in range(1, len(target)):
            if target[i] != cur:
                flips += 1
                cur = target[i]
        return flips
        