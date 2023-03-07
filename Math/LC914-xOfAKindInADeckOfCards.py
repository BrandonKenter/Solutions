class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = collections.Counter(deck)
        div = min(counts.values())

        if div < 2:
            return False
        for i in range(2, div+1):
            if all(count % i == 0 for count in counts.values()):
                return True
        return False
