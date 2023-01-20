class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)
        freq = [[] for i in range(6)]
        for rank, count in rank_counts.items():
            freq[count].append(rank)
        
        if len(suit_counts) == 1:
            return "Flush"
        elif len(freq[3]) == 1 or len(freq[4]) == 1:
            return "Three of a Kind"
        elif len(freq[2]) > 0:
            return "Pair"
        else:
            return "High Card"