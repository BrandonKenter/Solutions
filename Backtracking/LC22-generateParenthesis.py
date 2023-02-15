class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize result collection
        res = []
        # Initialize state collection
        combo = []

        # Create backtracking method
        def backtrack(open, close):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if open == n and close == n:
                res.append("".join(combo))
                return
            # Check if choice meets constraints before attempting choice
            # If choice does not meet constraints, continue (prune)
            if open > n or close > n:
                return
            
            # State is valid, so can proceed to make choice on this state
            # Choice to append '('
            # Reflect current choice in state collection
            combo.append('(')
            # Recurse on next choice space of next state
            backtrack(open + 1, close)
            # Clean up current choice (backtrack)
            combo.pop()
            
            # Check if choice meets constraints before attempting choice
            # If choice does not meet constraints, continue (prune)
            if close == open:
                return
            # Choice to append ')'
            combo.append(")")
            # Recurse on next choice space of next state
            backtrack(open, close + 1)
            # Clean up current choice (backtrack)
            combo.pop()
        
        backtrack(0, 0)
        return res