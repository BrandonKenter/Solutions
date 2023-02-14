class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length:
            return False
        
        # Initialize state collection
        sides = [0] * 4
        
        def backtrack(i):
            # Check if state is a Solution
            # Return True because asked if ONE solution exists
            if i == len(matchsticks):
                return True
            
            # Attempt to make a choice for every possible choice for the
            # current matchstick
            for j in range(4):
                # Base case check if the state using this choice is valid
                if matchsticks[i] + sides[j] <= length:
                    # State for this choice is valid, so update state
                    sides[j] += matchsticks[i]
                    # Add the if condition to return early since we only 
                    # care about finding ONE solution
                    if backtrack(i + 1):
                        return True
                    # Clean up choice (backtrack)
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)