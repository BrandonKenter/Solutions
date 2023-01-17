class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        while students:
            satisfied = False
            for i in range(len(students)):
                if students and students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.pop(0)
                    satisfied = True
                else:
                    student = students.popleft()
                    students.append(student)
            if not satisfied: break
        return len(students)