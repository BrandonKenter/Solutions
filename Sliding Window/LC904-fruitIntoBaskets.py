class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_counts = defaultdict(int)
        max_fruits = float('-inf')
        left = 0
        for right in range(len(fruits)):
            fruit_counts[fruits[right]] += 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[left]] -= 1
                if fruit_counts[fruits[left]] == 0:
                    fruit_counts.pop(fruits[left])
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits