class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        repeats = no_repeats_count = left = 0

        for right in range(len(s)):
            char_counts[s[right]] += 1
            if char_counts[s[right]] == 2: 
                repeats += 1

            if right - left + 1 == k:
                if repeats == 0: 
                    no_repeats_count += 1

                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 1: 
                    repeats -= 1
                left += 1
        return no_repeats_count
