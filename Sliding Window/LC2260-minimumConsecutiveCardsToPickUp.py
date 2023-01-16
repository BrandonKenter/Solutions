class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_counts = defaultdict(int)
        min_consec, cur_max_count, left = float('inf'), 0, 0
        for right in range(len(cards)):
            card_counts[cards[right]] += 1
            if card_counts[cards[right]] == 2:
                cur_max_count = 2
            
            while cur_max_count == 2:
                min_consec = min(min_consec, right - left + 1)
                card_counts[cards[left]] -= 1
                if card_counts[cards[left]] == 1: 
                    cur_max_count = 1
                left += 1
        return min_consec if min_consec != float('inf') else -1