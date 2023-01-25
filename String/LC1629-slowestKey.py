class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key_to_time = defaultdict(int)
        max_time, max_key = releaseTimes[0], keysPressed[0]

        key_to_time[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            key, time = keysPressed[i], releaseTimes[i] - releaseTimes[i-1]
            if time > max_time or (time == max_time and key > max_key):
                max_time = time
                max_key = key
        return max_key