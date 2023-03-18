class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        total_count = 0
        for num_same, count in counts.items():
            total_count += math.ceil(count / (num_same+1)) * (num_same+1)
        return total_count
