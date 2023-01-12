class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        left = 0
        for right in range(k-1, len(s)):
            code = s[left:right+1]
            codes.add(code)
            left += 1
        return True if len(codes) == 2**k else False