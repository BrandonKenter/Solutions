class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_h = []
        for cnt, char in [[-a, 'a'], [-b, 'b'], [-c, 'c']]:
            if cnt != 0:       
                heapq.heappush(max_h, [cnt, char])
        heapq.heapify(max_h)

        res = []
        while max_h:
            count, char = heapq.heappop(max_h)
            if len(res) > 1 and res[-2] == res[-1] == char:
                if len(max_h) == 0:
                    break
                count2, char2 = heapq.heappop(max_h)
                res.append(char2)
                count2 += 1
                heapq.heappush(max_h, [count, char])
                if count2 < 0: heapq.heappush(max_h, [count2, char2])
            else:
                res.append(char)
                count += 1
                if count < 0: heapq.heappush(max_h, [count, char])
        return "".join(res)