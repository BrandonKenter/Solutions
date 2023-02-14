class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        # Initialize result collection
        res = []
        # Initialize state collection
        cur_ip = []

        # Create backtracking method
        # State parameters: 
        #   - i where i is the index of the string s     
        def backtrack(i):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if i == len(s) and len(cur_ip) == 4:
                res.append(".".join(cur_ip))
                return

            # Base case to check if current state is valid
            if len(cur_ip) > 4:
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(i, min(i + 3, len(s))):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if (
                    int(s[i:j + 1]) >= 256 or
                    (i != j and s[i] == '0')
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collection
                cur_ip.append(s[i:j+1])
                # Recurse on next choice space of next state
                backtrack(j + 1)
                # Clean up current choice (backtrack)
                # i is automatically cleaned up because we are returning
                # to the previous execution context with previous arg
                cur_ip.pop()

        backtrack(0)
        return res
