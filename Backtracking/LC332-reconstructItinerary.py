class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        # Initialize state collection
        res = ['JFK']
        adj = defaultdict(list)
        for depart, dest in tickets:
            adj[depart].append(dest)

        # Create backtracking method
        # State parameters: 
        #   - cur where cur is the current airport
        def backtrack(cur):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if len(res) == len(tickets) + 1:
                return True

            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            temp = adj[cur]
            for i, nei in enumerate(temp):
                # Reflect current choice in state collections
                res.append(nei)
                adj[cur].pop(i)
                # Recurse on next choice space of next state
                # Add if condition and return value
                if backtrack(nei): 
                    return True
                # Clean up choice (backtrack)
                # cur is automatically cleaned up because we are returning
                # to the previous execution context with previous arg
                res.pop()
                adj[cur].insert(i, nei)
  
        backtrack('JFK')
        return res