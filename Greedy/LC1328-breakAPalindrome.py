class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                # Don't change middle char if string len is odd 
                # Because this doesn't break the palindrome
                if len(palindrome) % 2 and i == len(palindrome) // 2:
                    continue
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
        