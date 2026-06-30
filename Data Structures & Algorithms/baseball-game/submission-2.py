from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        result = 0
        for op in operations:
            if 'D' == op:
                stack.append(2 * stack[-1])
                result += stack[-1]
            elif 'C' == op:
                result -= stack[-1]
                stack.pop()
            elif '+' == op:
                stack.append(stack[-2] + stack[-1])
                result += stack[-1]
            else:
                number = int(op)
                stack.append(number)
                result += stack[-1]

        return result
        
