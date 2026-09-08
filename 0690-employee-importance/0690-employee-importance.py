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
        # id -- > employee object
        employee_map = {}
        for employee in employees:
            employee_map[employee.id] = employee

        total = 0
        q = deque([id])
        while q:
            id = q.popleft()
            employee = employee_map[id]
            total += employee.importance
            subordinates = employee.subordinates
            for subordinate in subordinates:
                q.append(subordinate)
        return total