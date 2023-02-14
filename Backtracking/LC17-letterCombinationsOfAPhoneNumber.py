class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_chars = {
                        '2' : 'abc',
                        '3' : 'def', 
                        '4' : 'ghi', 
                        '5' : 'jkl', 
                        '6' : 'mno', 
                        '7' : 'pqrs', 
                        '8' : 'tuv',
                        '9' : 'wxyz'
                        }
        # Initialize result collection
        res = []
        # Initialzie state collection
        combo = []

        # Create backtracking method
        # State parameters:
        #   - i where i is the index of the digits string
        def backtrack(i):
            # Check if state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if i == len(digits):
                res.append("".join(combo[:]))
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for char in dig_to_chars[digits[i]]:
                # Reflect current choice in state collection
                combo.append(char)

                ## Recurse on next choice space of next state
                backtrack(i+1)

                # Clean up current choice (backtrack)
                combo.pop()
        
        backtrack(0)
        return res if len(digits) != 0 else []
