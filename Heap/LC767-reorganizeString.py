class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counts = Counter(s)
        max_h = [[-c, char] for char, c in s_counts.items()]
        heapq.heapify(max_h)

        res = []
        prev = ""
        while max_h:
            cur_count, cur_char = heapq.heappop(max_h)
            if cur_char != prev:
                res.append(cur_char)
                cur_count += 1
                prev = cur_char
                if cur_count < 0: heapq.heappush(max_h, [cur_count, cur_char])
            else:
                if not max_h:
                    return ""
                cur_count2, cur_char2 = heapq.heappop(max_h)
                res.append(cur_char2)
                cur_count2 += 1
                prev = cur_char2
                heapq.heappush(max_h, [cur_count, cur_char])
                if cur_count2 < 0: heapq.heappush(max_h, [cur_count2, cur_char2])
        return "".join(res)