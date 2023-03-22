class Solution:
    def expand(self, s: str) -> List[str]:
        # Build an array to represent s in the format: [[a, b], [c], [d, e], [f]]
        # Allows us to write the backtrack logic easily
        chars = []
        i = j = 0
        while i < len(s):
            # If brace, get a list of all chars in the current braces
            if s[i] == '{':
                while s[j] != '}':
                    j += 1
                chars.append(s[i+1:j].split(","))
                i = j + 1
                j = i
            # Otherwise it's just a single char
            else:
                chars.append(s[i])
                i += 1
                j += 1
        
        # Backtrack to get all words
        res = [] # Result collection
        cur_word = [] # State collection
        def backtrack(i):
            # If at a solution state, append to the reuslt collection and return
            if i == len(chars):
                res.append("".join(cur_word))
                return
            
            # Iterate through all choices at this state
            for char in chars[i]:
                # Reflect the choice in the state collection
                cur_word.append(char)
                # Call backtrack on next choice space
                backtrack(i+1)
                # Undo choice
                cur_word.pop()
        
        backtrack(0)
        return sorted(res)
