class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        # Initialize state collection
        res = ['JFK']
        counts = defaultdict(int)
        adj = defaultdict(list)
        for depart, dest in tickets:
            adj[depart].append(dest)
            counts[(depart, dest)] += 1
        
        vis = defaultdict(int)

        # Create backtracking method
        # State parameters: 
        #   - cur where cur is the current airport
        def backtrack(cur, count):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if count == len(tickets):
                return True

            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for nei in adj[cur]:
                # Reflect current choice in state collections
                if vis[(cur, nei)] != counts[(cur, nei)]:
                    res.append(nei)
                    vis[(cur, nei)] += 1
                    # Recurse on next choice space of next state
                    # Add if condition and return value
                    if backtrack(nei, count + 1): 
                        return True
                    # Clean up choice (backtrack)
                    # cur is automatically cleaned up because we are returning
                    # to the previous execution context with previous arg
                    res.pop()
                    vis[(cur, nei)] -= 1
  
        backtrack('JFK', 0)
        return res
        
