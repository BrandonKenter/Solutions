class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        processing = deque() # (timeAvail, taskCount)
        taskCounts = Counter(tasks)
        avail = [-value for value in taskCounts.values()]
        heapq.heapify(avail)
        
        t = 0
        while avail or processing:
            t += 1
            
            if avail:
                task = heapq.heappop(avail)
                task += 1
                if task < 0:
                    processing.append((t + n, task))
            
            if processing and processing[0][0] == t:
                heapq.heappush(avail, processing.popleft()[1])
        return t
        