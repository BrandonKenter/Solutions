class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        t = 1
        while True:
            if memory1 >= memory2:
                if memory1 < t:
                    return [t, memory1, memory2]
                else:
                    memory1 -= t
            else:
                if memory2 < t:
                    return [t, memory1, memory2]
                else:
                    memory2 -= t
            t += 1
        