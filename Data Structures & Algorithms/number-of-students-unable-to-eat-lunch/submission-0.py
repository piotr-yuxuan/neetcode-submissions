from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(sandwiches)
        q1, q2 = deque(students), deque([])
        q1_len = len(q1)

        while q1:
            student = q1.popleft()
            if student == s[0]:
                s.popleft()
            else:
                q2.append(student)
            
            if q1_len == len(q2):
                break
            
            if not q1:
                q2, q1 = q1, q2
                q1_len = len(q1)
        
        return q1_len
