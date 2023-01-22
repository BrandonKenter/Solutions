class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_count = 0
        ast_count = 0
        for i, char in enumerate(s):
            if char == '|':
                bar_count += 1
            elif bar_count % 2:
                continue
            elif char == '*':
                ast_count += 1
        return ast_count