'''
BFS
'''
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        vis = set([start])
        q = deque([(start, 0)]) # (number, distance to this number)
        
        while q:
            cur_num, cur_dist = q.popleft()
            if cur_num == end:
                return cur_dist
            
            for mult in arr:
                new_num = (cur_num * mult) % mod
                new_dist = cur_dist + 1
                if new_num not in vis:
                    vis.add(new_num)
                    q.append((new_num, new_dist))
        return -1