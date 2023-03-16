'''
String for combo
Need to string join every combo before appending to res
Cleanup is just popping last digit in combo
Slower
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Create the backtracking method
        # State parameters:
        #   - i where i is the index of the current combination
        def backtrack(i):
            # Check if state is a solution
            # If so, add tto result collection
            # Return to previous choice space
            if i == n:
                res.append(int("".join(combo[:])))
                return

            # Iterate through choices for current state
            for j in range(0, 10):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if i == 0:
                    if j == 0: # constraint check (explicit continue statement)
                        continue
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    combo.append(str(j))
                    # Recurse on next choice space of next state
                    backtrack(i + 1)
                    # Clean up current choice (backtrack)
                    # i is automatically cleaned up because we are returning
                    #   to the previous execution context with previous arg
                    combo.pop()
                elif i > 0 and int(combo[-1]) - k == j: # constraint check (implicit continue statement)
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    combo.append(str(j))
                    # Recurse on next choice space of next state
                    backtrack(i + 1)
                    # Clean up current choice (backtrack)
                    # i is automatically cleaned up because we are returning
                    #   to the previous execution context with previous arg
                    combo.pop()
                elif i > 0 and int(combo[-1]) + k == j: # constraint check (implicit continue statement)
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    combo.append(str(j))
                    # Recurse on next choice space of next state
                    backtrack(i + 1)
                    # Clean up current choice (backtrack)
                    # i is automatically cleaned up because we are returning
                    #   to the previous execution context with previous arg
                    combo.pop()
        
        # Initialize result colleciton
        res = []
        # Initialize state collection
        combo = []
        # Call backtrack method with the starting state parameteters
        backtrack(0)
        return res
                

'''
Math for combo
Don't need string join for every combo before appending to res
No cleanup since all state is tracked via parameters
Faster
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Create the backtracking method
        # State parameters:
        #   - i where i is the index of the current combination
        def backtrack(i, combo, div):
            # Check if state is a solution
            # If so, add tto result collection
            # Return to previous choice space
            if i == n:
                res.append(combo)
                return

            # Iterate through choices for current state
            for j in range(0, 10):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if i == 0:
                    if j == 0: # constraint check (explicit continue statement)
                        continue
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    # Recurse on next choice space of next state
                    backtrack(i + 1, j, div * 10)
                    # Clean up current choice (backtrack)
                    # all params are automatically cleaned up because we are returning
                    #   to the previous execution context with previous args

                elif i > 0 and combo % 10 - k == j: # constraint check (implicit continue statement)
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    # Recurse on next choice space of next state
                    backtrack(i + 1, combo * 10 + j, div * 10)
                    # Clean up current choice (backtrack)
                    # all params are automatically cleaned up because we are returning
                    #   to the previous execution context with previous args
                elif i > 0 and combo % 10 + k == j: # constraint check (implicit continue statement)
                    # Choice meets constraints
                    # Reflect current choice in state collection
                    # Recurse on next choice space of next state
                    backtrack(i + 1, combo * 10 + j, div * 10)
                    # Clean up current choice (backtrack)
                    # all params are automatically cleaned up because we are returning
                    #   to the previous execution context with previous args

        # Initialize result colleciton
        res = []
        # Call backtrack method with the starting state parameteters
        backtrack(0, 0, 1)
        return res
                