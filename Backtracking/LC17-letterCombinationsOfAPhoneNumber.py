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
        res, combo = [], []

        def backtrack(i):
            # State is a solution, so add it to solution collection
            # Return to previous state
            if i == len(digits):
                res.append("".join(combo[:]))
                return
            
            # Iterate through next choices for current state
            for char in dig_to_chars[digits[i]]:
                # State is inherently valid, so update state
                combo.append(char)
                
                # Make next choice from current state by calling 
                # backtrack on next position in the digits string
                backtrack(i+1)

                # Clean up decision
                combo.pop()
        
        backtrack(0)
        return res if len(digits) != 0 else []
