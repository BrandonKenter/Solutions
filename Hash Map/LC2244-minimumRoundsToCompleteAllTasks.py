class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        rounds = 0
        for task, count in counts.items():
            if count == 1:
                return -1
            if count % 3 == 0: 
                rounds += count // 3
            else:
                rounds += count // 3 + 1
        return rounds