class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        par_to_child = defaultdict(list)
        for i in range(len(pid)):
            child = pid[i]
            par_to_child[ppid[i]].append(child)
        
        res = []
        q = deque([kill])
        while q:
            cur = q.popleft()
            res.append(cur)
            for child in par_to_child[cur]:
                q.append(child)
        return res