class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_consec = t_count = f_count = left = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T': t_count += 1
            else: f_count += 1

            to_flip = right - left + 1 - max(t_count, f_count)
            if to_flip <= k:
                max_consec = max(max_consec, right - left + 1)
            if to_flip > k:
                if answerKey[left] == 'T': t_count -= 1
                else: f_count -= 1
                left += 1
        return max_consec