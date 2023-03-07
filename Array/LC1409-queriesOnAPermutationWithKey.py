class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = deque([i for i in range(1, m + 1)])
        res = []
        for q in queries:
                res.append(p.index(q))
                p.remove(q)
                p.appendleft(q)
        return res
    