class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = [(ticket_count, i) for i, ticket_count in enumerate(tickets)]
        q = deque(tickets)
        time = 0
        while True: 
            time += 1
            ticket_count, i = q.popleft()
            ticket_count -= 1
            if ticket_count == 0:
                if i == k:
                    return time
            else:
                q.append((ticket_count, i))