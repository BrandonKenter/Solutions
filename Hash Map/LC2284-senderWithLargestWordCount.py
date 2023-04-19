class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        max_count = 0
        max_sender = None
        sen_counts = defaultdict(int)
        for i in range(len(messages)):
            m_len = len(messages[i].split())
            sen_counts[senders[i]] += m_len
            new_count = sen_counts[senders[i]]
            if new_count > max_count:
                max_count = new_count
                max_sender = senders[i]
            elif new_count == max_count:
                if senders[i] > max_sender: # lexographically larger
                    max_count = new_count
                    max_sender = senders[i]
        return max_sender
        