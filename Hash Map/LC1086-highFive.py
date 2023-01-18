class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = [None] * 1001

        for ID, score in items:
            if students[ID] is None:
                students[ID] = [score]
            else:
                heapq.heappush(students[ID], score)
                if len(students[ID]) > 5:
                    heapq.heappop(students[ID])
        res = []
        for ID in range(len(students)):
            if students[ID] != None:
                res.append([ID, sum(students[ID]) // 5])
        return res