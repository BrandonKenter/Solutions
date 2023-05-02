class Solution:
    def countPoints(self, rings: str) -> int:
        ring_sets = defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            color, ring_num = rings[i], rings[i+1]
            ring_sets[ring_num].add(color)
        
        num_rods = 0
        for ring_set in ring_sets.values():
            if len(ring_set) == 3:
                num_rods += 1
        return num_rods
        