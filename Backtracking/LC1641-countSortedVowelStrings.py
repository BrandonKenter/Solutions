# Explicit pick/not pick
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Initialize result variable
        res = 0
        # Initialize state collection
        combo = []

        # Create backtracking method
        def backtrack(i):
            nonlocal res
            if len(combo) == n:
                res += 1
                return
            
            # Check if state is valid
            if i == len(vowels):
                return

            # First choice: pick vowels[i]
            # Reflect choice in state collection
            combo.append(vowels[i])
            # Call backtrack on next choice space
            backtrack(i)

            # Clean up choice
            combo.pop()

            # Second choice: skip vowels[i]
            backtrack(i + 1)
        
        backtrack(0)
        return res
    

# For loop
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Initialize result variable
        res = 0
        # Initialize state collection
        combo = []

        # Create backtracking method
        def backtrack(i):
            nonlocal res
            if len(combo) == n:
                res += 1
                return
            # Check if state is valid
            if i == len(vowels):
                return

            for j in range(i, len(vowels)):
                combo.append(vowels[i])
                backtrack(j)
                combo.pop()

        backtrack(0)
        return res