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
            if i == len(digits):
                res.append("".join(combo[:]))
                return
            
            for char in dig_to_chars[digits[i]]:
                combo.append(char)
                backtrack(i+1)
                combo.pop()
        
        backtrack(0)
        return res if len(digits) != 0 else []