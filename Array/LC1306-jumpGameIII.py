class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        vis = set([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            prev_i = i - arr[i]
            next_i = i + arr[i]
            if prev_i in range(n) and prev_i not in vis: 
                q.append(prev_i)
                vis.add(prev_i)
            if next_i in range(n) and next_i not in vis:
                q.append(next_i)
                vis.add(next_i)
        return False
        