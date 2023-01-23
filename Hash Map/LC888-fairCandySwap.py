'''
        sx - x + y = sy - y + x
        y = x + (sy - sx) / 2
'''
class Solution:
    def fairCandySwap(self, alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
        sx, sy = sum(alice_sizes), sum(bob_sizes)

        set_y = set(bob_sizes)
        for x in alice_sizes:
            if x + (sy - sx) / 2 in set_y:
                return [x, x + (sy - sx) / 2]