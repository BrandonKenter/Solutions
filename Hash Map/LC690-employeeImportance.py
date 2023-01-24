"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.id_to_employee = {}
        for employee in employees:
            self.id_to_employee[employee.id] = employee
        
        total_importance = 0
        q = deque([self.id_to_employee[id]])
        while q:
            cur = q.popleft()
            total_importance += cur.importance

            for sub_id in cur.subordinates:
                q.append(self.id_to_employee[sub_id])
        return total_importance