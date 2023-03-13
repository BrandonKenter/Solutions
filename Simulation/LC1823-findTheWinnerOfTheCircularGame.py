class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [f for f in range(1, n + 1)]
        start = 0
        while len(friends) > 1:
            cur = start
            cur = (cur + k - 1) % len(friends)
            friends.pop(cur)
            start = cur % len(friends)
        return friends[0]
