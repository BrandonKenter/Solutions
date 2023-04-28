class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        # Initialize state collection
        res = ['JFK']
        ticket_counts = defaultdict(int) # The total counts for each ticket (source, destination)
        cur_ticket_counts = defaultdict(int) # Acts as a visited set but encodes frequency for backtracking
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
            ticket_counts[(source, dest)] += 1
        
        # Create backtracking method
        # State parameters: 
        #   - cur where cur is the current airport
        #   - cur_ticket_count where count is the count of tickets used so far
        def backtrack(cur, cur_ticket_count):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if cur_ticket_count == len(tickets):
                return True

            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for nei in adj[cur]:
                # Reflect current choice in state collections
                if cur_ticket_counts[(cur, nei)] != ticket_counts[(cur, nei)]:
                    res.append(nei)
                    cur_ticket_counts[(cur, nei)] += 1
                    # Recurse on next choice space of next state
                    # Add if condition and return value
                    if backtrack(nei, cur_ticket_count + 1): 
                        return True
                    # Clean up choice (backtrack)
                    # cur is automatically cleaned up because we are returning
                    # to the previous execution context with previous arg
                    res.pop()
                    cur_ticket_counts[(cur, nei)] -= 1
  
        backtrack('JFK', 0)
        return res
