class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        q = deque([a for a in arr])
        
        wins = 0
        while True:
            left, right = q.popleft(), q.popleft()
            if left > right:
                wins += 1
                if wins == k:
                    return left
                q.appendleft(left)
                q.append(right)
            else:
                wins = 1
                if wins == k:
                    return right
                q.appendleft(right)
                q.append(left) 
