class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        repeat_set = set()
        repeats = no_repeats_count = left = 0

        for right in range(len(s)):
            char_counts[s[right]] += 1
            if char_counts[s[right]] >= 2 and s[right] not in repeat_set: 
                repeats += 1
                repeat_set.add(s[right])

            if right - left + 1 == k:
                if repeats == 0: 
                    no_repeats_count += 1

                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 1: 
                    repeats -= 1
                    repeat_set.remove(s[left])
                left += 1
        return no_repeats_count