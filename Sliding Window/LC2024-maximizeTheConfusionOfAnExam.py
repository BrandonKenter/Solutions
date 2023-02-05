'''
Using explicit T/F counter variables
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_consec = t_count = f_count = left = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T': t_count += 1
            else: f_count += 1

            to_flip = right - left + 1 - max(t_count, f_count)
            if to_flip <= k:
                max_consec = max(max_consec, right - left + 1)
            else:
                if answerKey[left] == 'T': t_count -= 1
                else: f_count -= 1
                left += 1
        return max_consec
    
'''
Using defaultdict
This implementation is a bit more concise
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer_counts = defaultdict(int)
        max_consec = left = 0
        for right in range(len(answerKey)):
            answer_counts[answerKey[right]] += 1
            if (right - left + 1) - max(answer_counts.values()) > k:
                answer_counts[answerKey[left]] -= 1
                left += 1
            else:
                max_consec = max(max_consec, right - left + 1)
        return max_consec
