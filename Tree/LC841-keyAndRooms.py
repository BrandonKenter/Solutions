class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = 1
        vis = set([0])
        q = deque([0])
        while q:
            cur = q.popleft()
            for key in rooms[cur]:
                if key not in vis:
                    q.append(key)
                    vis.add(key)
                    count += 1
        return count == len(rooms)