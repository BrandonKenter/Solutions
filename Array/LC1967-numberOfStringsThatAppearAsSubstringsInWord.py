'''
O(N*M^2)
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        patterns_count = Counter(patterns)
        count = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                substr = word[i:j+1]
                if substr in patterns_count:
                    count += patterns_count[substr]
                    patterns_count.pop(substr)
        return count


'''
O(N*M)
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count