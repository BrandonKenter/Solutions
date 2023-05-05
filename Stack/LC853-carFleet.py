class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = deque()
        
        for car in sorted(cars)[::-1]:
            pos, sp = car[0], car[1]
            arrival_t = (target - pos) / sp
            stack.append(arrival_t)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)