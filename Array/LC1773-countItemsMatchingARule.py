class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for t, c, n in items:
            if ruleKey == "type" and ruleValue == t:
                count += 1
            elif ruleKey == "color" and ruleValue == c:
                count += 1
            elif ruleKey == "name" and ruleValue == n:
                count += 1
        return count
        