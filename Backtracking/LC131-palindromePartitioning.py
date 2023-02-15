class Solution:
    def is_palindrome(self, substring):
        left, right = 0, len(substring) - 1
        while left <= right:
            if substring[left] == substring[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


    def partition(self, s: str) -> List[List[str]]:
        # Initialize result collection
        res = []
        # Initialize state collection
        partition = []

        # Create backtracking method
        def backtrack(i):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if i == len(s):
                res.append(partition[:])
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(i, len(s)):
                substring = s[i:j+1]
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if not self.is_palindrome(substring):
                    continue
                
                # Choice meets constraints
                # Reflect current choice in state collection
                partition.append(substring)
                # Recurse on next choice space of next state
                backtrack(j + 1)
                # Clean up current choice (backtrack)
                # i is automatically cleaned up because we are returning
                # to the previous execution context with previous arg
                partition.pop()
        
        backtrack(0)
        return res