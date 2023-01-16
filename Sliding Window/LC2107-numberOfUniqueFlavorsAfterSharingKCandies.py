class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        my_counts = Counter(candies) 
        if k == 0: return len(my_counts)

        my_max_unique = float('-inf') 
        left = 0
        for right in range(len(candies)):
            my_counts[candies[right]] -= 1
            if my_counts[candies[right]] == 0:
                my_counts.pop(candies[right])
            
            if right - left + 1 == k:
                my_max_unique = max(my_max_unique, len(my_counts))
                my_counts[candies[left]] += 1
                left += 1
        return my_max_unique