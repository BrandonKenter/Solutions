class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        count = 0
        while left <= right:
            s = people[left] + people[right]
            if s > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            count += 1
        return count
        